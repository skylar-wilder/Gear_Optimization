import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# GIVEN PARAMETERS
# -----------------------------
a = 100.0
T = 150.0
n = 1450.0
phi = np.radians(20)

E = 206e3
nu = 0.3

sigma_b_allow = 220.0
sigma_c_allow = 900.0

Ko = 1.25
Ks = 1.0
KH = 1.6
Qv = 6

m_SN = 3.5
m_c = 6
N0 = 1e7

# -----------------------------
# FUNCTIONS
# -----------------------------
def geometry(i, m):
    Z1 = (2 * a) / (m * (1 + i))
    Z2 = i * Z1
    rp1 = a / (1 + i)
    rp2 = a * i / (1 + i)
    return Z1, Z2, rp1, rp2

def pitch_velocity(rp1):
    return (np.pi * rp1 * n) / 30.0 / 1000.0

def tangential_load(rp1):
    return T / (rp1 / 1000.0)

def dynamic_factor(V):
    A = 50 + 56 * (1 - Qv / 12)
    return ((A + np.sqrt(V)) / A) ** 2

def geometry_factor_J(Z):
    return 0.32 * np.log(Z) - 0.16

def geometry_factor_I(i):
    return (np.cos(phi) * np.sin(phi) / 2) * (i / (1 + i))

def elastic_coefficient():
    return np.sqrt(E / (2 * np.pi * (1 - nu**2)))

def contact_ratio(rp1, rp2, m):
    ra1 = rp1 + m
    ra2 = rp2 + m
    rb1 = rp1 * np.cos(phi)
    rb2 = rp2 * np.cos(phi)

    return (
        np.sqrt(ra1**2 - rb1**2)
        + np.sqrt(ra2**2 - rb2**2)
        - a * np.sin(phi)
    ) / (np.pi * m * np.cos(phi))

def bending_stress(Ft, Kv, b, m, J):
    return (Ft * Ko * Ks * KH * Kv) / (b * m * J)

def contact_stress(Ft, Kv, b, dp, I):
    ZE = elastic_coefficient()
    return ZE * np.sqrt((Ft * Ko * Kv * Ks * KH) / (b * dp * I))

def bending_life(sigma_b):
    return (sigma_b_allow / sigma_b) ** m_SN * N0

def contact_life(sigma_c):
    return (sigma_c_allow / sigma_c) ** m_c * N0

# -----------------------------
# EVALUATION
# -----------------------------
def evaluate_design(i, m, b):
    Z1, Z2, rp1, rp2 = geometry(i, m)

    if Z1 < 17:
        return None

    V = pitch_velocity(rp1)
    Ft = tangential_load(rp1)
    Kv = dynamic_factor(V)

    J = geometry_factor_J(Z1)
    I = geometry_factor_I(i)
    dp = 2 * rp1

    eps = contact_ratio(rp1, rp2, m)
    if eps < 1.2:
        return None

    sigma_b = bending_stress(Ft, Kv, b, m, J)
    sigma_c = contact_stress(Ft, Kv, b, dp, I)

    Nb = bending_life(sigma_b)
    Nc = contact_life(sigma_c)

    life = min(Nb, Nc)

    return life, sigma_b, sigma_c

# -----------------------------
# GRID SEARCH + DATA LOGGING
# -----------------------------
modules = [1.5, 2, 2.5, 3, 4, 5, 6, 8]
ratios = np.linspace(1.0, 3.0, 50)
b_factors = np.linspace(8, 12, 5)

life_data = []
i_data = []
m_data = []
b_data = []

best = -1
best_params = None

for m in modules:
    for i in ratios:
        for bf in b_factors:
            b = bf * m

            result = evaluate_design(i, m, b)
            if result is None:
                continue

            life, sb, sc = result

            # store for plotting
            life_data.append(life)
            i_data.append(i)
            m_data.append(m)
            b_data.append(b)

            if life > best:
                best = life
                best_params = (i, m, b)

print("\nBest Design:")
print("i =", best_params[0])
print("m =", best_params[1])
print("b =", best_params[2])
print("Life =", best)

# -----------------------------
# PLOTTING FUNCTIONS
# -----------------------------

# -----------------------------
# CLEAN SUBPLOT VISUALIZATION
# -----------------------------
def plot_all():

    fig, axs = plt.subplots(2, 2)
    fig.suptitle("Optimization Landscape")

    # -----------------------------
    # 1. Life vs Gear Ratio
    # -----------------------------
    sorted_data = sorted(zip(i_data, life_data))
    i_sorted, life_sorted = zip(*sorted_data)

    axs[0, 0].plot(i_sorted, life_sorted)
    axs[0, 0].set_title("Life vs Gear Ratio")
    axs[0, 0].set_xlabel("Gear Ratio (i)")
    axs[0, 0].set_ylabel("Life")
    axs[0, 0].grid()

    # -----------------------------
    # 2. Life vs Module
    # -----------------------------
    sorted_data = sorted(zip(m_data, life_data))
    m_sorted, life_sorted = zip(*sorted_data)

    axs[0, 1].plot(m_sorted, life_sorted)
    axs[0, 1].set_title("Life vs Module")
    axs[0, 1].set_xlabel("Module (m)")
    axs[0, 1].set_ylabel("Life")
    axs[0, 1].grid()

    # -----------------------------
    # 3. Life vs Face Width
    # -----------------------------
    sorted_data = sorted(zip(b_data, life_data))
    b_sorted, life_sorted = zip(*sorted_data)

    axs[1, 0].plot(b_sorted, life_sorted)
    axs[1, 0].set_title("Life vs Face Width")
    axs[1, 0].set_xlabel("Face Width (b)")
    axs[1, 0].set_ylabel("Life")
    axs[1, 0].grid()

    # -----------------------------
    # 4. Life progression (search order)
    # -----------------------------
    axs[1, 1].plot(life_data)
    axs[1, 1].set_title("Life During Search")
    axs[1, 1].set_xlabel("Iteration")
    axs[1, 1].set_ylabel("Life")
    axs[1, 1].grid()

    plt.tight_layout()
    plt.show()

plot_all()