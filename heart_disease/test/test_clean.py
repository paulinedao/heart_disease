"""
Module for testing
"""
import sys
import os
import unittest
import pandas as pd 
import numpy as np

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, package_dir)

from src.load import load_data
from src.process import process_all
from src.clean import clean_all
from src.clean import impute_nan


class TestClean(unittest.TestCase):
    
    @classmethod
    # load the dataframe to use it as a test
    
    def setUp(cls): 

        processed_df = process_all('data/raw_data/processed.cleveland.data')
        cls._df = clean_all(processed_df)
        
    def test_impute_nan(self):
        # test that the number of columns with null values is null
       col_with_na =  self._df.isna().any().sum()
       
       self.assertEqual(col_with_na, 0)
        
    def test_clean_all(self):
        # create test data
        import pandas as pd

        # Create a test dataframe with some duplicate entries
        self.df = pd.DataFrame(data = {
        'A': [1, 2, np.nan, 1, 2, np.nan],
        'B': ['cat1', 'cat2', np.nan, 'cat1', 'cat2', np.nan],
        'C': [True, False, np.nan, True, False, np.nan],
        'D': ['d1', 'd2', 'd3', 'd1', 'd2', 'd3']})

        # use clean_all function
        self.df = clean_all(self.df)
        
        # define col_with_na 
        col_with_na =  self.df.isna().any().sum()
        
        # test that there are no columns with null values
        self.assertEqual(col_with_na, 0)

        # test that the number of duplicated is null
        duplicated_entries = self.df.duplicated().sum() 
        
        self.assertEqual(duplicated_entries, 0)
      
if __name__ == '__main__':
    unittest.main()