"""
Module to test handling outliers
"""
import sys
import os
import unittest
import pandas as pd

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, package_dir)

from src.outlier import outlier_report_handle


class TestOutlier(unittest.TestCase):
    def setUp(self):
        # Create a test dataframe containing outliers
        self.df = pd.DataFrame(
            {
                "A": [1, 2, 3, 4, 5, 100],
                "B": [1, 2, 3, 4, 5, 7],
                "C": [1, 2, 3, 4, 5, 7],
            }
        )

    def test_outlier_report_handle_1(self):
        """ Checks that the dataframe 
        after handling outliers with 
        a z-score=2 is equal
        to the expected one"""
        
        df_test_1 = outlier_report_handle(self.df, 2)

        output_df1 = pd.DataFrame(
            {"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [1, 2, 3, 4, 5]}
        )

        pd.testing.assert_frame_equal(df_test_1.reset_index(drop=True), output_df1)

    def test_outlier_report_handle_2(self):
        """ Checks that the dataframe 
        after handling outliers with 
        a z-score=2 is equal
        to the expected one"""
        
        df_test_2 = outlier_report_handle(self.df, 3)

        output_df2 = pd.DataFrame(
            {
                "A": [1, 2, 3, 4, 5, 100],
                "B": [1, 2, 3, 4, 5, 7],
                "C": [1, 2, 3, 4, 5, 7],
            }
        )

        pd.testing.assert_frame_equal(df_test_2.reset_index(drop=True), output_df2)


if __name__ == "__main__":
    unittest.main()
