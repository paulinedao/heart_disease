"""
    
Module to handle outliers
    
"""

import numpy as np
import pandas as pd
from scipy import stats


def outlier_report(df, zscorethreshold):
    """
    For each column with outliers,
    the dataframe with the values is returned.

    Args:
        df (dataframe): numerical dataframe
        zscorethreshold (float): z-score threshold 
        
    """
    
    outliers_df = []
    indexvals = []
    outliers_columns = []
    
    for column in df.columns:
        mean_column = np.mean(df[column])
        sd_column = np.std(df[column])   
        
        # pull out outliers
        outliers = df.loc[((abs(df[column]-mean_column))/sd_column) > zscorethreshold]
        
        # select columns with outliers and add infos to the lists
        if len(outliers) == 0:
            pass
        else:
            outliers_df.append(outliers.values)
            indexvals.append(outliers.index.values)
            outliers_columns.append(column)

    # print report per column
    for number, item in enumerate(outliers_df):
        print('\nData points with outliers in column {}\n'.format(outliers_columns[number]))
    
        df = pd.DataFrame(outliers_df[number], index=indexvals[number], columns=df.columns)
        
        print(df)
        print(f'\nValues of outliers: {df[outliers_columns[number]].values}')
        print(f'\nIndex values of outliers as a list: {indexvals[number]}')
        print('---------------------------------------------------------------------------')
    
def handle_outliers(df, zscorethreshold):
    """
    Erases outliers using
    zscore strategy. 

    Args:
        df (dataframe): numerical dataframe
        zscorethreshold (float): z-score threshold
    """
    
    df = df[(np.abs(stats.zscore(df)) < zscorethreshold).all(axis=1)]

    return df