#import staments
import numpy as np
import pandas as pd
import seaborn as sns


#Reading file
file = pd.read_csv("C:/Users/vyasn/OneDrive/Desktop/Academics/Project_1/P2504_1_Standings/P2504_1_standings_1.csv")

print(file.head(),"\n")

# General info about the dataset
print(file.info(),"\n")

# Check for null values
print(file.isnull().sum(),"\n")
file['year'] = file['year'].fillna(method='ffill')
print(file.isnull().sum(),"\n")
file = file.dropna()
print(file.isnull().sum(),"\n")
































