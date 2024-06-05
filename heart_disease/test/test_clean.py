"""
Module for testing
"""

import unittest
from heart_disease.src.clean import impute_nan
from heart_disease.src.clean import clean_all

class TestClean(self):
    
    @classmethod
    # load the dataframe to use it as a test
    
    def setUp(cls): 
        cls._df = load_data('../data/raw_data/processed.cleveland.data')
        #cls._df = pd.read_csv('../data/raw_data/processed.cleveland.data')
    
    def test_impute_nan(self):
        # test that the number of columns with null values is null
       col_with_na =  df_clean.isna().any().sum()
       
       self.assertEqual(col_with_na, 0)
        
    def test_clean_all(self):
        # test that the number of duplicated and na values is null
        duplicated_entries = df.duplicated().sum() 
        
        self.assertEqual(duplicated_entries, 0)
      
if __name__ == '__main__':
    unittest.main()