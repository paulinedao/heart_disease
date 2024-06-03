"""
    
Module with plotting functions
    
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
   
def make_count_plots(df, columns):
    """
    Makes countplots of a variable
    to visualize its distribution.
    
    Args:
        df (dataframe): name of the dataframe you want to use
        columns (list): takes a list of columns to visualize the variables
    """
    
    for column in columns:
        sns.countplot(data = df, x = column)
        plt.ylabel('number of patients')
        plt.title(f'Distribution of {column}')
        plt.show()
    
   

def hist_plot_numericals(df): # not tested
    """
    Plots histograms for 
    each numerical variable
    of the dataset

    Args:
        df (dataframe): name of the dataframe you want to use
    """
    # Distinguish the dataset between numerical and categorical variables
    categorical_columns = ['chest_pain', 'st_slope', 'thallium_stress_test', 'rest_ecg']
    boolean_columns = ['sex', 'high_fasting_blood_sugar', 'exercise_angina']
    
    # Creating a figure for subplotting 
    fig, axes = plt.subplots(ncols = 6, figsize=(30, 6))

    # creating a loop to display histograms of numerical variables
    for ax, column in zip(axes, df.drop(columns=categorical_columns+boolean_columns).columns):
        if "heart_disease_diagnosis" in column: continue
        sns.histplot(data = df, x = column, hue = "heart_disease_diagnosis", bins = 25, stat = "percent", common_norm = False, palette ="viridis", ax = ax)
    
    plt.tight_layout()
    plt.show()
    
def plot_pie_chart(df, column):
    """
    Plots pie chart for categorical variables
    in the healthy or heart disease group.
    
    Args:
        df: name of the dataframe you want to use
        column (string): name of the column
    """
    heart_disease = df[df['heart_disease_diagnosis'] == 1]
    no_heart_disease = df[df['heart_disease_diagnosis'] == 0] 
      
    fig = plt.figure(figsize = (10,10))
    fig.add_subplot(1,2,1)
    heart_disease[column].value_counts().sort_index().plot(kind = 'pie', autopct = '%1.1f%%')
    fig.add_subplot(1,2,2)
    no_heart_disease[column].value_counts().sort_index().plot(kind = 'pie', autopct = '%1.1f%%')
    plt.title(f'percentage of {column} in heart disease group (left) and healthy group (right)')
    plt.show()
    
def contingency_table(data, column):
    """
    Makes contingency table for categorical variables
    and heart_disease_diagnosis
    and plots it into a heatmap.

    Args:
        data (dataframe): name of the dataframe you want to use
        column (string): name of the column
    """
    data_crosstab = pd.crosstab(index=[data[column]], columns=data['heart_disease_diagnosis'])
    fig = plt.figure(figsize = (10,10))
    fig.add_subplot()    
    sns.heatmap(data_crosstab, cmap = 'RdYlGn')
    plt.show()
    
def look_for_correlations(df):
    """
    Plots a pairplot for numerical variables,
    and a heatmap to look at correlations.
    
    Arg:
        df (dataframe): name of the dataframe you want to use
    """
    num_df = df.select_dtypes(include='number')
    num_df['heart_disease_diagnosis']=df['heart_disease_diagnosis']
    
    sns.pairplot(num_df, kind = 'reg', hue = 'heart_disease_diagnosis', corner = True)
    plt.show()
    
    sns.heatmap(num_df.corr(), cmap = 'RdYlGn', vmin = -0.5, vmax =0.5)
    plt.show()