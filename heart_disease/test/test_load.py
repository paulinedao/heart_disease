"""
Module to test loading
"""
import sys
import os
import unittest

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, package_dir)

import pandas as pd
from src.load import load_data
from src.load import describe_data


class TestLoad(unittest.TestCase):
    @classmethod
    # load the dataframe to use it as a test
    def setUp(cls):
        cls._df = load_data("data/raw_data/processed.cleveland.data")

    def test_load_data(self):
        """ Checks that a dataframe is loaded
        and that the column names are correct
        """
        
        # check if the loaded data type is a dataframe
        self.assertIsInstance(self._df, pd.DataFrame)

        # define expected column names
        column_list = [
            "age",
            "sex",
            "chest_pain",
            "rest_blood_pressure",
            "serum_cholesterol",
            "fasting_blood_sugar",
            "rest_ecg",
            "max_heart_rate_thal",
            "exercise_angina",
            "st_oldpeak",
            "st_slope",
            "nb_major_vessels",
            "thallium_stress_test",
            "heart_disease_diagnosis",
        ]

        # check that column names were added properly
        self.assertListEqual(list(self._df.columns), column_list)


if __name__ == "__main__":
    unittest.main()
