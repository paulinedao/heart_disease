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
        df (dataframe): dataframe
        zscorethreshold (float): z-score threshold 
        
    """
    # select numerical features from the given dataframe
    df = df.select_dtypes(include='number')
    
    outliers_info = []
    
    for column in df.columns:
        mean_column = np.mean(df[column])
        sd_column = np.std(df[column])   
        
        # pull out outliers from dataframe
        outliers = df.loc[((abs(df[column]-mean_column))/sd_column) > zscorethreshold]
        
        # Add outliers infos to the lists
        if len(outliers) == 0:
            pass
        else:
            outliers_info.append((column, outliers))

    # print report per column
    for column, outlier in outliers_info:
        print(f'\nData points with outliers in column {column}\n')
            
        print(outliers)
        print(f'\nValues of outliers: {outliers[column].values}')
        print(f'\nIndex values of outliers as a list: {list(outliers.index)}')
        print('---------------------------------------------------------------------------')
    
def handle_outliers(df, zscorethreshold):
    """
    Erases outliers using
    zscore strategy. 

    Args:
        df (dataframe): dataframe
        zscorethreshold (float): z-score threshold
    """

    # select numerical features from the given dataframe
    df_numerical = df.select_dtypes(include='number')
    
    
    # calculate z-score of the numerical dataframe
    z_scores = np.abs(stats.zscore(df_numerical))

    # create a filter using the z-score as threshold
    kept_rows = (z_scores < zscorethreshold).all(axis=1)
    
    df_new  = df[kept_rows]

    return df_new      

def outlier_report_handle(df, zscorethreshold):
    outlier_report(df, zscorethreshold)
    df = handle_outliers(df, zscorethreshold)
    return df