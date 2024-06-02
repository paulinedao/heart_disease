"""
    
Module with plotting functions
    
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
   
def plot_pie_chart(df, column):
    """_summary_
    plot pie chart for categorical variables
    Args:
        df: dataframe
        column (name of the column): type string
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
    """_summary_

    Args:
        data (dataframe): write the dataframe you are working on
        column (string): write the name of the column
    """
    data_crosstab = pd.crosstab(index=[data[column]], columns=data['heart_disease_diagnosis'])
    fig = plt.figure(figsize = (10,10))
    fig.add_subplot()    
    sns.heatmap(data_crosstab, annot = True, fmt="d", cmap = 'RdYlGn')
    plt.show()