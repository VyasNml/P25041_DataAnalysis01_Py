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


#Objective 1
#Selecting Required data
file['rank'] = file.groupby('year')['points_differential'].rank(method='first', ascending=False)
top3_file = file[file['rank'] <= 3]
top3_file['rank'] = top3_file['rank'].astype(int)

#Implementing Line Plot
plt.figure(figsize=(14, 6))
sns.lineplot(data=top3_file, x='year', y='points_differential', hue='rank', style='rank', marker='o', dashes=True)
plt.title('Top 3 Teams by Points Differential Across Seasons (Rank-wise)')
plt.xlabel('Year')
plt.ylabel('Points Differential')
plt.legend(title='Rank')
plt.show()

# Objective 2



plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=file_filtered,
    x='offensive_ranking',
    y='defensive_ranking',
    hue='team_name',  
    palette='tab10',
    alpha=0.7
)

plt.title('Offensive vs Defensive Rankings of Teams')
plt.xlabel('Offensive Ranking (Lower is Better)')
plt.ylabel('Defensive Ranking (Lower is Better)')
plt.grid(True)
plt.tight_layout()
plt.show()


























