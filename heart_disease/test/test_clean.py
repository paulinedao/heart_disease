"""
Module for testing
"""
import sys
import os
import unittest

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, package_dir)

from src.clean import impute_nan
from src.clean import clean_all



class TestClean(unittest.TestCase):
    
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