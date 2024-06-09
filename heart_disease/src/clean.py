"""
Module to handle duplicates, 
clean missing values, and
impute values in the dataset.
"""
import os
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


def impute_nan(df):
    """
    Handles NaNs with different strategies
    depending on the data type,
    and returns df_clean without NaNs
    as a dataframe, with the correct datatypes.

    Args:
        df (dataframe): write the name of the dataframe
    """

    # Define numerical categorical and boolean lists
    numerical_features = df.select_dtypes(include="number").columns
    categorical_features = df.select_dtypes(include="category").columns
    boolean_features = df.select_dtypes(include="bool").columns

    df[boolean_features] = df[boolean_features].astype("int")

    # Prepare the transformer with the imputers
    preprocess_columns = ColumnTransformer(
        transformers=[
            ("imputer_numeric", SimpleImputer(strategy="median"), numerical_features),
            (
                "imputer_categoric",
                SimpleImputer(strategy="most_frequent"),
                categorical_features,
            ),
            ("imputer_bool", SimpleImputer(strategy="most_frequent"), boolean_features),
        ]
    )

    # Fit the model to the dataset
    preprocess_columns.fit(df)

    # Transform the columns in train and test set
    data_column_transformed = preprocess_columns.transform(df)

    # Create list with the same order of variables
    input_features = (
        list(numerical_features) + list(categorical_features) + list(boolean_features)
    )

    df_clean = pd.DataFrame(data=data_column_transformed, columns=input_features)

    #reassign categories
    df_clean[boolean_features] = df_clean[boolean_features].astype("bool")
    df_clean[numerical_features] = df_clean[numerical_features].astype("float64")
    df_clean[categorical_features] = df_clean[categorical_features].astype("category")

    df.to_csv("data/processed_data/clean_data.csv")
    
    return df_clean


def clean_all(df):
    """
    Drops duplicates and handles NaNs.
    Assumes that the processing of the
    dataframe has been done beforehand.

    Args:
        df (dataframe): write the name of the dataframe
    """
    df.drop_duplicates(inplace=True)
    df_clean = impute_nan(df)
    return df_clean
