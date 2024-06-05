# Heart disease Project

# Table of Contents



## Description
The heart_disease package was written to process the dataset to be able to visualize the data and draw insights from it. 

The package contains modules to load and process the data and generate plots. Check the jupyter notebook 'heart_disease.ipynb' here [report](heart_disease/heart_disease.ipynb)

## Installation

The heart_disease package was built using a virtual environment. To set up the virtual environment for the project, activate your virtual environment and use the requirements.txt file.

### Requirements

Install the requirements for the project using this code in the terminal:

```bash
pip install -r requirements.txt
```

### Download the package heart_disease

clone the repository
```bash
git clone [github url]
```

Locate the directory of the package and change the current directory to where the package is located using:
```bash
cd heart_disease_directory
```

## Run the package
The package has been parsed to allow the user to run the whole package or only selected part.
### Run parts
The package contains 3 modules:
1. load
2. process
3. plotting

The 'process' module will load the data before processing the data. The 'plotting' module will run the loading and processing modules before plotting.

To load and process the data, write:
```bash
python3.11 main.py --process
```

To generate plots, write:
```bash
python3.11 main.py --plot
```

To clean the data, write:
```bash
python3.11 main --clean
```

### Run all

To run all, write:
```bash
python3.11 main.py --all
```

