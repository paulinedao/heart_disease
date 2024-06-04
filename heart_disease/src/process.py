"""
Module to process the dataframe, 
renaming, replacing categories' or column names, 
and changing variable types
"""
from src.load import *

def process_categorical_columns(df):
    """
    For categorical variables, 
    rewrites names of each category
    instead of having an arbitrary value.
    Change variables type to 'category'.
    The variable 'sex' is treated as
    categorical to have understandable
    labels.

    Args:
        df (dataframe): write the name of the dataframe 
    """
    # Give categories names instead of a arbitrary value for categorical variables
    df['chest_pain'].replace({1: 'typical angina', 2: 'atypical angina', 3: 'non-anginal pain', 4: 'asymptomatic'}, inplace=True )
    df['rest_ecg'].replace({0: 'normal', 1: 'ST-T wave abnormality', 2: 'probable or definite LV hypertrophy'}, inplace = True)
    df['st_slope'].replace({1: 'upsloping',  2: 'flat', 3: 'downsloping'}, inplace = True)
    df['thallium_stress_test'].replace({3 : 'normal', 6 : 'fixed defect', 7 : 'reversable defect'}, inplace = True)
    df['sex'].replace({0 : 'female', 1 : 'male'}, inplace = True)
    
    # Change variables type to 'category'
    df[['sex', 'chest_pain','st_slope', 'thallium_stress_test', 'rest_ecg']] = df[['sex', 'chest_pain','st_slope', 'thallium_stress_test', 'rest_ecg']].astype('category')
    
    return df

def process_boolean_columns(df):
    """
    For boolean variables,
    converts the type einto boolean
    and renames the columns.

    Args:
        df (dataframe): write the name of the dataframe
    """
    # modify diagnosis columns: from 1-4 to 1 to indicate presence of heart disease with 1 and absence with 0
    for i in range(1,5):
        df['diagnosis'].replace(i, 1, inplace = True)
    
    # Replace the type of 'fasting_blood_sugar', 'exercise_angina' and 'diagnosis' with boolean type
    df[['fasting_blood_sugar', 'exercise_angina', 'diagnosis']] = df[['fasting_blood_sugar', 'exercise_angina', 'diagnosis']].astype(bool)
    
    # Renaming column names using  df.rename(columns={'oldName1': 'newName1', 'oldName2': 'newName2'}, inplace=True)
    df.rename(columns={'fasting_blood_sugar': 'high_fasting_blood_sugar', 'diagnosis': 'heart_disease_diagnosis'}, inplace=True)
    
    return df

def process_all(path):
    df=load_data(path)
    
    process_categorical_columns(df)
    process_boolean_columns(df)
    df.to_csv('data/processed_data/processed_data')
    return df
