# Heart disease Project

# Table of Contents



## Description
The heart_disease package was written to process the dataset to be able to visualize the data and draw insights from it. 

The package contains modules to load and process the data and generate plots. Check the jupyter notebook 'heart_disease.ipynb' here [report](heart_disease/heart_disease.ipynb)

## Installation

The heart_disease package was built using a virtual environment. To set up the virtual environment for the project, use the requirements.txt file.

### Requirements
Install the requirements for the project using this code, in the terminal where you activated the virtual environment:

```bash
pip install -r requirements.txt
```

### Install the package heart_disease
Locate the directory of the package and change the current directory to where the package is located using:
```bash
cd heart_disease_directory
```

Install the package:
```bash
pip install
```

## Run the package
The package has been parsed to allow the user to run the whole package or only selected part.
### Run parts
The package contains 3 modules:
1. load
2. process
3. plotting

The process argument will load the data before processing the data. The plotting module will run the loading and processing modules before plotting.

To load and process the data, write:
```bash
python3.11 heart_disease/main.py --process
```

To generate plots, write:
```bash
python3.11 heart_disease/main.py --plot
```

### Run all

To run all, write:
```bash
python3.11 heart_disease/main.py --all
```