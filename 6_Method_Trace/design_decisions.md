The development of the optimization model involved several key design decisions to balance accuracy, computational efficiency, and clarity of analysis.

First, a parametric approach was adopted using three primary design variables: gear ratio i, module m, and face width b. These were selected because they directly influence both bending and contact stresses while allowing the rest of the gear geometry to be derived analytically from the fixed center distance constraint.

A grid search method was chosen for optimization instead of gradient-based techniques. This decision was made to ensure full exploration of the design space and avoid convergence to local optima. Although computationally less efficient, this approach provides a clear visualization of the objective landscape and guarantees identification of the global optimum within the chosen resolution. And since the module must be kept an integer, the need for adding a constraint was removed and thus a less complicated model was made. 

AGMA-based stress models were used for both bending and contact stress calculations. This ensures that the analysis is consistent with industry-standard practices and provides physically meaningful results. Simplified geometry factor expressions were used in place of tabulated values to enable efficient computation across a large number of design iterations.

The face width was constrained within a proportional range (8m≤b≤12m) to maintain realistic gear proportions while still allowing flexibility for optimization. This range reflects commonly used design guidelines rather than strict physical limits.

The gear ratio was treated as a free variable to explore its influence on stress and fatigue life. While this leads to a mathematical optimum at i=1, it is acknowledged that in practical applications the gear ratio is typically dictated by system requirements.
