#import staments
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 3.1 Reading file
df = pd.read_csv("C:/Users/vyasn/OneDrive/Desktop/Academics/Project_1/P2504_1_Standings/P2504_1_standings_1.csv")

# Printing to check if read() was succesfull
print(df.head(),"\n")

# 3.2 General info about the dataset
print(df.info(),"\n")

# Check for null values
print(df.isnull().sum(),"\n")

# 3.3 Handling Missing Values
df['year'] = df['year'].fillna(method='ffill')
print(df.isnull().sum(),"\n")

df = df.dropna()
print(df.isnull().sum(),"\n")

#3.4.	Statistical Summary
print(df.describe())


######### Objective 1 #########
# 4.1: Analyze how team wins have changed across different seasons to identify performance trends.

#Selecting Required data
# 4.1.1 Rank teams by points_differential within each year
file['rank'] = file.groupby('year')['points_differential'].rank(method='first', ascending=False)
# 4.1.2: Keep only top 3 ranks
top3_file = file[file['rank'] <= 3]
# 4.1.3: Convert rank to integer
top3_file['rank'] = top3_file['rank'].astype(int)

#Implementing Line Plot
plt.figure(figsize=(14, 6))
# 4.1.4: Plot the top 3 ranks
sns.lineplot(data=top3_file, x='year', y='points_differential', hue='rank', style='rank', marker='o', dashes=True)
# Titles and labels
plt.title('Top 3 Teams by Points Differential Across Seasons (Rank-wise)')
plt.xlabel('Year')
plt.ylabel('Points Differential')
plt.legend(title='Rank')
plt.show()

######### Objective 2 #########
# 4.2: Compare points scored versus points conceded to evaluate offensive and defensive strengths

# Calculate the average points scored and conceded for each team
avg_points = file.groupby('team_name')[['points_for', 'points_against']].mean().reset_index()

# Create the scatter plot
plt.figure(figsize=(10, 8))
sns.scatterplot(data=avg_points, x='points_for', y='points_against', hue='team_name', s=100)
plt.title('Average Offensive vs. Defensive Strengths (Aggregated)')
plt.xlabel('Average Points Scored')
plt.ylabel('Average Points Conceded')
plt.grid(True)
plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()



######### Objective 3 #########
# 4.3: Explore the distribution and variation of victory margins among teams.

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

######### Objective 4 #########
# 4.4: Examine correlations between key performance metrics to discover influential factors

# Set plot size
plt.figure(figsize=(10, 6))

# Create histogram
sns.histplot(data=file, x='points_for', bins=30, kde=True, color='skyblue')

# Add titles and labels
plt.title('Distribution of Points Scored by Teams', fontsize=14)
plt.xlabel('Points Scored')
plt.ylabel('Number of Teams')
plt.tight_layout()

plt.show()


######### Objective 5 #########
# 4.5: Examine correlations between key performance metrics to discover influential factors.

# Step 1: Select only the most relevant columns
selected_cols = ['wins', 'points_for', 'points_against', 'margin_of_victory',
                 'simple_rating', 'strength_of_schedule']

# Step 2: Create a subset dataframe
subset_data = file[selected_cols]

# Step 3: Calculate correlation matrix
corr_matrix = subset_data.corr()

# Step 4: Plot the refined heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Key Performance Metrics')
plt.tight_layout()
plt.show()

#Heatmap
sns.pairplot(file[['wins', 'points_for', 'points_against', 'margin_of_victory', 'simple_rating']])
plt.suptitle('Pairwise Relationships Between Key Metrics', y=1.02)
plt.show()




















