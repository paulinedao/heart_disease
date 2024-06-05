# Heart disease Project

# Table of Contents



## Description
The heart_disease package was written to process the dataset to be able to visualize the data and draw insights from it. 

The package contains modules to load, process the data, generate plots and clean the dataset. Check the jupyter notebook 'heart_disease.ipynb' here [report](heart_disease/heart_disease.ipynb)

## Organization of the package
The package heart_disease contains a module 'main' as well as the report. There are 4 modules to prepare the data located in 'heart_disease/src'. The original dataset is in 'heart_disease/data/raw_data/processed.cleveland.data'.

## Installation

### Download the package heart_disease

clone the repository
```bash
git clone [github url]
```

Navigate to the project directory:
```bash
cd heart_disease
```
### Requirements
The heart_disease package was built using a virtual environment. To set up the virtual environment for the project, activate your virtual environment and use the requirements.txt file.
Install the requirements for the project using this code in the terminal:

```bash
pip install -r requirements.txt
```

## Run the package
The package has been parsed to allow the user to run the whole package or only selected part.
### Run parts
The package contains 3 modules:
1. load
2. process
3. plotting

The 'process' module will load the data before processing the data. 
To load and process the data, write:
```bash
python3.11 main.py --process
```

To run the 'plotting' module you need to process the data beforehand. To generate plots, write:
```bash
python3.11 main.py --plot
```

To run the 'clean' module, the data needs to be processed beforehand. To clean the data, write:
```bash
python3.11 main --clean
```

### Run all
To run all, write:
```bash
python3.11 main.py --all
```
### Input
The first module 'load' takes the path to the file to load and saves the dataframe into df. The othere modules take the dataframe df. 

### Output
The output of load and process is the dataframe, where the processing steps have been done on the file. The plotting module outputs 8 plots to answer questions that are written in the [report][heart_disease.ipynb].


## Modularity and reusability
### Modules organization
The 4 modules 'load', 'process', 'plotting', 'clean' are in the folder 'src'. Here's the path to find each of them:
- 'load' functions are in heart_disease/src/load.py
- 'process' functions are in heart_disease/src/process.py
- 'plotting' functions are in heart_disease/src/plotting.py
- 'clean' functions are in heart_disease/src/clean.py

### Reusability
This package was written to proceess the Cleveland dataset from UC Irvine Machine Learning Repository. The generated plots using the function 'plot_all(df)' will genrate per default 8 plots, to answer the questions mentionned in the [report]. 

However, th user is free to use the plotting functions to visualize other features by specifying the 'columns' argument for each function.

## Run unit tests
A unit test was developed for each module to verify the basic functionning of the code.

```bash
python3.11 test/test_load.py
python3.11 test/test_process.py
python3.11 test/test_plotting.py
python3.11 test/test_clean.py
```
