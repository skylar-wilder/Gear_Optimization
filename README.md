# Gear Optimization

## Project Overview

This project focuses on optimizing gear parameters and configurations to achieve efficient mechanical performance. The codebase provides tools and algorithms for analyzing, simulating, and optimizing various gear-related metrics and designs.

## Folder Structure

```
Gear_Optimization/
├── 1_Report/                      #Final Paper to cite
├── 2_Presentation/                #Presentation on the Final Paper
├── 3_Code/                        #Simulation Code
├── 4_Data_Results/                #Data used as input and received outputs
├── 5_Literature/                  #A few Literature pieces reviwed for the project
├── 6_Method_Trace/                #Modeling Desicisions
├── 7_Reproducibility/             #Reproducing in your own PC
└── README.md
```


## Instructions to Run the Code

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Numpy
- Matplotlib

### Setup

1. Clone the repository:
```bash
git clone https://github.com/skylar-wilder/Gear_Optimization.git
cd Gear_Optimization
```

2. Run the main optimization script:
```bash
python 3_code/ME701.py
```


## Location of Main Results

All optimization results, outputs and inputs are saved to the `4_Data_Results/` directory. Key output files include:

- **Reference and Initialization** : in the subfolder `Input data/` include both the files with the data chosen.
- **Main result** : the final optimized value and a comparision of the same with the baseline are present in the subfolder `processed data/`.
- **Outputs** - the .stp files for the gears used as reference and the optimized gears are both present in the `outputs/` subfolder
- **Plots** - the plots of how Life varies with teh design variables and through different iterations is given in the `plots/` subfolder

For detailed analysis and explaination of the theory used, refer to the report in the `1_Report/` directory.

## Contributing

For questions or contributions, please open an issue or submit a pull request.

---

**Last Updated:** 2026-05-05
