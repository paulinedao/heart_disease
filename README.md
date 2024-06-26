# Heart disease Project

# Table of Contents
- [Description](#description)
- [Organization of the package](#organization-of-the-package)
- [Installation](#installation)
  - [Download the package heart_disease](#download-the-package-heart-disease)
  - [Requirements](#requirements)
- [Run the package](#run-the-package)
  - [Run parts](#run-parts)
  - [Run all](#run-all)
  - [Input](#input)
  - [Output](#output)
- [Modularity and reusability](#modularity-and-reusability)
  - [Modules organization](#modules-organization)
  - [Reusability](#reusability)
- [Run unit tests](#run-unit-tests)


## Description
The heart_disease package was written to process the [Cleveland Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease?fbclid=IwAR3RjwfHPg251wjyPMZjGrU1OFZxp-Odh6g6LJTjLSiuDln91k-BUoMVssY) to be able to visualize the data and draw insights from it. 

The package contains modules to load, process the data, generate plots and clean the dataset. Check the [jupyter notebook 'heart_disease.ipynb'](heart_disease/heart_disease.ipynb)

## Organization of the package
The package heart_disease contains a module 'main' as well as the report. There are 4 modules to prepare the data located in 'heart_disease/src'. The original dataset is in 'heart_disease/data/raw_data/processed.cleveland.data'.

## Installation

### Download the package heart_disease

clone the repository
```bash
git clone https://github.com/paulinedao/heart_disease.git
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
The package contains several modules:
1. load
2. process
3. clean
4. outlier
5. plotting

The 'process' module will load the data before processing the data. 
To load and process the data, write:
```bash
python main.py --process
```

To run the 'plotting' module you need to process the data beforehand. To generate plots, write:
```bash
python main.py --plot
```

To module 'clean' is used on thee processed dataset. To clean the data, write:
```bash
python main --clean
```

### Run all
To run all, write:
```bash
python main.py --all
```
### Input
The first module 'load' takes the path to the file to load and returns a pandas dataframe. 

### Output
The output of load and process is the dataframe, where the processing steps have been done on the file. After the processing, the file is saved as 'processed_data.csv' in the folder 'data/processed_data'. After cleaning, the file is saved as 'clean_data.csv' in the same folder 'data/processed_data'.  The plotting module outputs several plots to answer questions that are written in the [report](heart_disease/heart_disease.ipynb).


## Modularity and reusability
### Modules organization
The 4 modules 'load', 'process', 'plotting', 'clean' are in the folder 'src'. Here's the path to find each of them:
- 'load' functions are in heart_disease/src/load.py
- 'process' functions are in heart_disease/src/process.py
- 'plotting' functions are in heart_disease/src/plotting.py
- 'clean' functions are in heart_disease/src/clean.py

### Reusability
This package was written to proceess the Cleveland dataset from UC Irvine Machine Learning Repository. The generated plots using the function 'plot_all(df)' will generate per default several plots, to answer the questions mentionned in the [report](heart_disease/heart_disease.ipynb). 

However, the user is free to use the plotting functions to visualize other features by specifying the 'columns' argument for each function.

## Run unit tests
A unit test was developed for each module to verify the basic functionning of the code.

```bash
python test/test_load.py
python test/test_process.py
python test/test_plotting.py
python test/test_clean.py
```

To check the coverage of the test:
```bash
pip install coverage
```
```bash
coverage run -m unittest test_name.py
```
To generate a report:
```bash
coverage report -m
```
## License
The code in this repository is licensed under the [MIT License](LICENSE.md).