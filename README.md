# Gear Optimization

## Project Overview

This project focuses on optimizing gear parameters and configurations to achieve efficient mechanical performance. The codebase provides tools and algorithms for analyzing, simulating, and optimizing various gear-related metrics and designs.

## Folder Structure

```
Gear_Optimization/
├── README.md                 # Project documentation and setup instructions
├── src/                      # Main source code directory
├── data/                     # Input data and test cases
├── results/                  # Generated results and outputs
├── tests/                    # Unit tests and validation scripts
└── requirements.txt          # Python dependencies
```

**Note:** Adjust the folder structure above to match your actual project layout.

## Instructions to Run the Code

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/skylar-wilder/Gear_Optimization.git
cd Gear_Optimization
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the main optimization script:
```bash
python src/main.py
```

### Running Tests

To verify the implementation:
```bash
python -m pytest tests/
```

## Location of Main Results

All optimization results and outputs are saved to the `results/` directory. Key output files include:

- **Optimization logs**: `results/optimization_log.txt`
- **Performance metrics**: `results/metrics.json`
- **Optimized parameters**: `results/optimized_config.csv`
- **Visualizations**: `results/plots/` (graphs and charts)

For detailed analysis, refer to the generated reports in the `results/` directory after running the optimization scripts.

## Contributing

For questions or contributions, please open an issue or submit a pull request.

---

**Last Updated:** 2026-05-05
