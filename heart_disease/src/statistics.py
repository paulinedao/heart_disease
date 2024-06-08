import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

def chi_square_stats(data, column):
    """
    Calculates the Chi2, p-value,
    degre of freedom and expected
    frequencies

    Args:
        data (dataframe): name of the dataframe
        column (string): column name
    """
    # create contingency table
    data_crosstab = pd.crosstab(index=[data[column]], columns=data['heart_disease_diagnosis'])
    
    # chi2 test
    chi2_stats, pvalue, dof, expected_freq = chi2_contingency(data_crosstab)
    
    # print values
    print('Chi2 statistics: ', chi2_stats)
    print('p-value: ', pvalue)
    print('Degree of freedom: ', dof)
    print('Expected frequencies: ', expected_freq)
    