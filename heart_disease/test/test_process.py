"""
Module for testing
"""

import sys
import os
import unittest

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, package_dir)

from src.process import process_categorical_columns
from src.process import process_boolean_columns
from src.process import process_all


class TestProcess(unittest.TestCase):
    @classmethod
    # load the dataframe to use it as a test
    def setUp(cls):
        cls._df = process_all("data/raw_data/processed.cleveland.data")

    def test_process_categorical_columns(self):
        # Check that the type of the column is 'category'
        categorical_columns = [
            "sex",
            "chest_pain",
            "st_slope",
            "thallium_stress_test",
            "rest_ecg",
        ]
        for column in categorical_columns:
            self.assertEqual(self._df.dtypes[column], "category")

    def test_process_boolean_columns(self):
        # Check that the type of the column is 'bool'
        boolean_columns = [
            "fasting_blood_sugar",
            "exercise_angina",
            "heart_disease_diagnosis",
        ]
        for column in boolean_columns:
            self.assertEqual(self._df.dtypes[column], "bool")

    def test_process_all(self):
        # Check that the file has been created
        self.assertTrue(os.path.exists("data/processed_data/processed_data.csv"))


if __name__ == "__main__":
    unittest.main()
