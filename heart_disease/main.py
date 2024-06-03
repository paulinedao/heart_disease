"""
Main module for the projet
"""
import argparse
import os
from src.plotting import *
from src.load import *
from src.process import *





# Make count plots for the variables 'heart_disease_diagnosis'
# make_count_plots(df, ['sex', 'heart_disease_diagnosis'])

# hist_plot_numericals(df, hue_variable = 'heart_disease_diagnosis')

# categorical_columns = ['chest_pain', 'st_slope', 'thallium_stress_test', 'rest_ecg']
# boolean_columns = ['sex', 'high_fasting_blood_sugar', 'exercise_angina']

# for column in categorical_columns:
#     plot_pie_chart(df, column)

# contingency_table(df, column)

# look_for_correlations(df)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Heart Disease project")
    parser.add_argument("--process", action="store_true", help="Process the dataset")
    parser.add_argument("--plot", action="store_true", help="Generate the requested plots")
    parser.add_argument('--all', action='store_true', help='Run all blocks')
    
    args = parser.parse_args()
    
    if args.process:
        df = process_all('data/raw_data/processed.cleveland.data')
        print(df.head())
        
    if args.plot:
        if os.path.exists('data/processed_data/processed_data'):
            df = pd.read_csv('data/processed_data/processed_data')
            print(df.head())
        else:
            df = process_all('data/raw_data/processed.cleveland.data')

        make_count_plots(df, ['sex', 'heart_disease_diagnosis'])

        hist_plot_numericals(df, hue_variable = 'heart_disease_diagnosis')

        categorical_columns = ['chest_pain', 'st_slope', 'thallium_stress_test', 'rest_ecg']
        boolean_columns = ['sex', 'high_fasting_blood_sugar', 'exercise_angina']

        for column in categorical_columns:
            plot_pie_chart(df, column)

        for column in boolean_columns:
            contingency_table(df, column)

        look_for_correlations(df)
