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


# Objective 3

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

# Objective 4

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


# Objective 5




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




















