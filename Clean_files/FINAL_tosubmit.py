# How can the European bank identify and predict key factors driving customer churn, and what strategies can be implemented to reduce churn based on customer profiles and behavior patterns?

# IMPORTS
import sys 
sys.setrecursionlimit(1500)

import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from scipy import stats

# LOADING THE DATA 
df = pd.read_csv('churn_bank.csv')
    # Creating two seperate datasets for future analysis
dfStayed = df.loc[df['Exited']==1]
dfExited = df.loc[df['Exited']==0]

