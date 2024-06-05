"""
Module for testing
"""
import sys
import os
import unittest

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0, package_dir)

from heart_disease.src.load import load_data
from heart_disease.src.load import describe_data

class TestLoad(unittest.TestCase): 
    @classmethod
    # load the dataframe to use it as a test
    def setUp(cls): 
        cls._df = load_data('../data/raw_data/processed.cleveland.data')
        
        # cls._df = pd.read_csv('../data/raw_data/processed.cleveland.data')
    
    def test_load_data(self): 

        self.assertIsInstance(cls._df, df)
        
        # define expected column names
        column_list = ['age', 'sex', 'chest_pain', 'rest_blood_pressure', 'serum_cholesterol', 
                       'fasting_blood_sugar', 'rest_ecg','max_heart_rate_thal', 'exercise_angina', 
                       'st_oldpeak', 'st_slope', 'nb_major_vessels', 'thallium_stress_test', 'diagnosis'
                       ]
        
        # check that column names were added properly
        self.assertListEqual(list(df.columns), column_list)
 

if __name__ == '__main__':
    unittest.main()

