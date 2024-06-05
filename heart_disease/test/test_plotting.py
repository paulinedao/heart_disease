"""
Module for testing
"""
import sys
import os
import unittest


package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.insert(0, package_dir)

from heart_disease.src.plotting import make_count_plots
from heart_disease.src.plotting import hist_plot_numericals
from heart_disease.src.plotting import plot_pie_chart
from heart_disease.src.plotting import contingency_table
from heart_disease.src.plotting import look_for_correlations
from heart_disease.src.plotting import plot_all

class TestPlotting(unittest.TestCase):
    @classmethod
    # load the dataframe to use it as a test
    def setUp(cls): 
        cls._df = load_data('../data/raw_data/processed.cleveland.data')
        #cls._df = pd.read_csv('../data/raw_data/processed.cleveland.data')
        
    def test_make_count_plots(self):
        # Check if the function executes without errors
        make_count_plots(self.df)

    def test_hist_plot_numericals(self):
        # Check if the function executes without errors
        hist_plot_numericals(self.df)
        
    def test_plot_pie_chart(self):
        # Check if the function executes without errors
        plot_pie_chart(self.df)
        
    def test_contingency_table(self):
        # Check if the function executes without errors
        contingency_table(self.df)
        
    def test_look_for_correlations(self):
        # Check if the function executes without errors
        look_for_correlations(self.df)
        
if __name__ == '__main__':
    unittest.main()