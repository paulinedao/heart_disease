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
    as a dataframe.
     
    Args:
        df (dataframe): write the name of the dataframe
    """
    
    # Define numerical categorical and boolean lists
    numerical_features = df.select_dtypes(include='number').columns
    categorical_features = df.select_dtypes(include='category').columns
    boolean_features = df.select_dtypes(include='bool').columns
    
    df[boolean_features] = df[boolean_features].astype("int")
    
    # Prepare the transformer with the imputers        
    preprocess_columns = ColumnTransformer(transformers=[('imputer_numeric',
                                        SimpleImputer(strategy='median'),
                                        numerical_features),
                                        ('imputer_categoric',
                                        SimpleImputer(strategy='most_frequent'),
                                        categorical_features),
                                        ('imputer_bool',
                                        SimpleImputer(strategy='most_frequent'),
                                        boolean_features)])
    
    # Fit the model to the dataset
    preprocess_columns.fit(df)
    
    # Transform the columns in train and test set
    data_column_transformed = preprocess_columns.transform(df)
    
    df_clean = pd.DataFrame(data=data_column_transformed, columns=df.columns)
    
    df_clean[boolean_features] = df[boolean_features].astype("bool")

    return df_clean

def clean_all(df):
    """
    Drops duplicates and handles
    NaNs.

    Args:
        df (_type_): _description_
    """
    if os.path.exists('../data/processed_data/processed_data'):
        df = pd.read_csv('../data/processed_data/processed_data')
        print(df.head())
    else:
        df = process_all('../data/raw_data/processed.cleveland.data')
        
    df.drop_duplicates(inplace=True)
    impute_nan(df)

# import os
#df.to_excel(path.join('data/processed_data/clean_data'), index = False)
# df.ExcelWriter(path)