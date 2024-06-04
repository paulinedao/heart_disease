"""
Module to clean missing values of the dataset,
impute values and normalize the dataset.
"""
    
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

def impute_nan(df):
    """
    function to handle NaNs according to the data type
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