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
    
   

def hist_plot_numericals(df, hue_variable = 'heart_disease_diagnosis'): 
    """
    Plots histograms for 
    each numerical variable
    of the dataset

    Args:
        df (dataframe): name of the dataframe you want to use
    """
    # Distinguish the dataset between numerical and categorical variables

    num_df = df.select_dtypes(include='number')
    total_numericals = len(num_df.columns)

    num_df[hue_variable]=df[hue_variable]
    # Creating a figure for subplotting 
    fig, axes = plt.subplots(ncols=total_numericals, figsize=(30, 6))

    # creating a loop to display histograms of numerical variables
    for ax, column in zip(axes, num_df.columns):
        if hue_variable in column: continue
        sns.histplot(data = df, x = column, hue = hue_variable, bins = 25, stat = "percent", common_norm=False, ax = ax)
    
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
    

    # Pie plot for heart_disease group  
    fig = plt.figure(figsize = (10,10))
    fig.add_subplot(1,2,1)
    heart_disease[column].value_counts().sort_index().plot(kind = 'pie', autopct = '%1.1f%%', radius=0.8, wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'})
    plt.ylabel('') # Hide y-label
    
    # Pie plot for no_heart_disease group
    fig.add_subplot(1,2,2)
    no_heart_disease[column].value_counts().sort_index().plot(kind = 'pie', autopct = '%1.1f%%', radius=0.8, wedgeprops={'linewidth': 3.0, 'edgecolor': 'white'})
    plt.ylabel('')
    
    plt.title(f'percentage of {column} in heart disease group (left) and healthy group (right)', loc='left')
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