"""
Module for testing
"""

import sys
import os
import unittest

package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0, package_dir)

from src.process import process_all
from src.plotting import make_count_plots
from src.plotting import hist_plot_numericals
from src.plotting import plot_pie_chart
from src.plotting import contingency_table
from src.plotting import look_for_correlations
from src.plotting import plot_all

class TestPlotting(unittest.TestCase):
    @classmethod
    # load the dataframe to use it as a test
    def setUp(cls): 
        cls._df = process_all('data/raw_data/processed.cleveland.data')
        
    def test_make_count_plots(self):
        # Check if the function executes without errors
        make_count_plots(self._df, ['heart_disease_diagnosis'])

    def test_hist_plot_numericals(self):
        # Check if the function executes without errors
        hist_plot_numericals(self._df)
        
    def test_plot_pie_chart(self):
        # Check if the function executes without errors
        plot_pie_chart(self._df, 'st_slope')
        
    def test_contingency_table(self):
        # Check if the function executes without errors
        contingency_table(self._df, 'exercise_angina')
        
    def test_look_for_correlations(self):
        # Check if the function executes without errors
        look_for_correlations(self._df)
        
if __name__ == '__main__':
    unittest.main()