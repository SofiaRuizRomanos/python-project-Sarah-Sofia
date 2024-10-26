import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

####

def plot_density(
    data, 
    x_col, 
    hue_col=None, 
    fill=True, 
    title=None, 
    xlabel=None, 
    ylabel='Density'):
    """
    Generates a density plot for a given dataset.

    Parameters (those are the inputs you have to enter in your main code):
    - data: the dataset to plot
    - x_col: the column to plot the density for
    - hue_col: the column to group data by different categories (e.g., 'Geography')
    - fill: whether to fill the area under the curve (default: True)
    - title: the title of the plot
    - xlabel: the label for the x-axis
    - ylabel: str, optional, the label for the y-axis (default: 'Density')
    """

    sns.kdeplot(data=data, x=x_col, hue=hue_col, fill=fill)
    
    # Set plot title and labels
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    else:
        plt.xlabel(x_col)
    plt.ylabel(ylabel)
    

    plt.show()