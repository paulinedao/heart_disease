"""
Module to load the data   
"""

import pandas as pd


def load_data(path):
    """
    load the data and creates the column names
    Args:
        path (string): path to the data
    """
    df = pd.read_csv(path, header=None, na_values="?")

    df.columns = [
        "age",
        "sex",
        "chest_pain",
        "rest_blood_pressure",
        "serum_cholesterol",
        "fasting_blood_sugar",
        "rest_ecg",
        "max_heart_rate_thal",
        "exercise_angina",
        "st_oldpeak",
        "st_slope",
        "nb_major_vessels",
        "thallium_stress_test",
        "heart_disease_diagnosis",
    ]

    return df


def describe_data(df):
    """_summary_

    Args:
        df (_type_): _description_
    """

    shape_of_data = df.shape
    print(f"The number of (rows,columns) in this dataset is {shape_of_data}.")
    print(" ")

    print("Information about columns names and types")
    print(df.info())

    print(" ")
    print("statistics summary of the dataset")
    print(df.describe())
