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

# Drop rows with nulls in the relevant columns
file_filtered = file.dropna(subset=['margin_of_victory', 'playoffs'])


plt.figure(figsize=(10, 6))
sns.boxplot(
    data=file_filtered,
    x='playoffs',
    y='margin_of_victory',
    palette='Set2'
)

plt.title('Margin of Victory: Playoff vs Non-Playoff Teams')
plt.xlabel('Playoff Status')
plt.ylabel('Margin of Victory')
plt.grid(True)
plt.tight_layout()
plt.show()


#Objective 3

# Group data by year and calculate average margin of victory
avg_margin_by_year = file.groupby('year')['margin_of_victory'].mean().reset_index()

# Set plot size
plt.figure(figsize=(10, 6))

# Create the bar plot
sns.barplot(data=avg_margin_by_year, x='year', y='margin_of_victory', palette='coolwarm')

# Add titles and labels
plt.title('Average Margin of Victory Over the Years', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Average Margin of Victory')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()






















