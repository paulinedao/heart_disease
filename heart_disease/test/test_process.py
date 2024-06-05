"""
Module for testing
"""

import sys
import os
import unittest

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0, package_dir)

from src.process import process_categorical_columns
from src.process import process_boolean_columns
from src.process process_all
        
class TestProcess(unittest.TestCase):
    @classmethod
    # load the dataframe to use it as a test
    def setUp(cls): 
        cls._df = load_data('../data/raw_data/processed.cleveland.data')
        #cls._df = pd.read_csv('../data/raw_data/processed.cleveland.data')

        
    def test_process_categorical_columns(self):
        processed_df = process_categorical_columns(self._df)
        categorical_columns = ['sex', 'chest_pain','st_slope', 'thallium_stress_test', 'rest_ecg']
        self.assertTrue(processed_df[categorical_columns].dtypes.equals(category))

        
    def test_process_boolean_columns(self):
        processed_df = process_boolean_columns(self._df)
        boolean_columns = ['high_fasting_blood_sugar', 'exercise_angina', 'heart_disease_diagnosis']
        self.assertTrue(processed_df[categorical_columns].dtypes.equals(bool))

    def test_process_all(self):
        self.assertTrue(os.path.exists('data/processed_data/processed_data'))
        


if __name__ == '__main__':
    unittest.main()