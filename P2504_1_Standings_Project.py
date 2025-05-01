#import staments
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 3.1 Reading file
df = pd.read_csv("C:/Users/vyasn/OneDrive/Desktop/Academics/Project_1/P2504_1_Standings/INT375 Project 12304075/INT375_Standings.csv")

# Printing to check if read() was succesfull
print("     Printing to check if read() was succesfull\n")
print(df.head(),"\n")

# 3.2 General info about the dataset
print("     General info about the dataset\n")
print(df.info(),"\n")


# Check for null values
print("     Check for null values\n")
print(df.isnull().sum(),"\n")

# 3.3 Handling Missing Values
print("     Correcting Missing values in 'Year' column using forward fill\n")
df['year'] = df['year'].fillna(method='ffill')
print(df.isnull().sum(),"\n")

print("Dropping Missing values")
df = df.dropna()
print(df.isnull().sum(),"\n")

#3.4.	Statistical Summary
print(df.describe())

while True:
    print("\nInput corresponding objective number to display visualization")
    print("     1   -> Objective 1")
    print("     2   -> Objective 2")
    print("     3   -> Objective 3")
    print("     4   -> Objective 4")
    print("     5   -> Objective 5")
    print("     6   -> EXIT")
    n = int(input(" Enter you choice: "))
    if n==1:
        
        ##### OBJECTIVE 1 #####
        # 4.1.	Objective 1 : Analyze how team wins have changed across different seasons to identify performance trends.
        print("\nObjective 1 : Analyze how team wins have changed across different seasons to identify performance trends.")
        # 4.1.1 Rank teams by points_differential within each year
        df['rank'] = df.groupby('year')['points_differential'].rank(method='first', ascending=False)
        # print(df['rank'])


        # 4.1.2: Keep only top 3 ranks
        top3_file = df[df['rank'] <= 3]

        # 4.1.3: Convert rank to integer
        top3_file['rank'] = top3_file['rank'].astype(int)

        # 4.1.4: Plot the top 3 ranks
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=top3_file, x='year', y='points_differential', hue='rank', style='rank', marker='o', dashes=True)

        # Titles and labels
        plt.title('Top 3 Teams by Points Differential Across Seasons (Rank-wise)')
        plt.xlabel('Year')
        plt.ylabel('Points Differential')
        plt.legend(title='Rank')

        print("\nDisplaying Line Plot...")
        plt.show()
        print("\nDisplay closed")


    if n==2:
        #ad
        ##### OBJECTIVE 2 #####
        # 4.2.	Objective 2: Compare points scored versus points conceded to evaluate offensive and defensive strengths
        print("\nObjective 2: Compare points scored versus points conceded to evaluate offensive and defensive strengths")

        # 4.2.1: Calculate the average points scored and conceded for each team
        avg_points = df.groupby('team_name')[['points_for', 'points_against']].mean().reset_index()

        # 4.2.2: Create the scatter plot
        plt.figure(figsize=(10, 8))
        sns.scatterplot(data=avg_points, x='points_for', y='points_against', hue='team_name')

        # Titles and labels
        plt.title('Average Offensive vs. Defensive Strengths (Aggregated)')
        plt.xlabel('Average Points Scored')
        plt.ylabel('Average Points Conceded')
        plt.grid(True)
        plt.legend(title='Team', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()

        print("\nDisplaying Scatter Plot...")
        plt.show()
        print("\nDisplay closed")


    if n==3:
        ##### OBJECTIVE 3 #####
        print("\nObjective 3: Explore the distribution and variation of victory margins among teams.")

        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='margin_of_victory',kde = True, bins=20)  

        plt.title('Distribution of Victory Margins Across All Teams')
        plt.xlabel('Margin of Victory')
        plt.ylabel('Frequency')
        plt.grid(True)

        print("\nDisplaying Histogram...")
        plt.show()
        print("\nDisplay closed")


    if n==4:
        ##### OBJECTIVE 4 #####
        print("\nObjective 4: Examine correlations between key performance metrics to discover influential factors.")


        # Select only the relevant numeric columns
        corr_matrix = df[['wins','loss','margin_of_victory', 'points_for', 'points_against', 'points_differential']].corr()

        # Plot Heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='YlGnBu', fmt='.2f', square=True)
        plt.title('Correlation Heatmap of Key Performance Metrics')
        plt.tight_layout()

        print("\nDisplaying Heatmap...")
        plt.show()
        print("\nDisplay closed")


    if n==5:
        ##### OBJECTIVE 5 #####
        print("\nObjective 5: Identify and compare the strongest overall teams based on their ratings and schedules.")

        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, x='team_name', y='simple_rating')

        plt.title('Distribution of Team Ratings Across All Teams')
        plt.xlabel('Team Name')
        plt.ylabel('Rating')
        plt.xticks(rotation=90)  # Rotate x-axis labels for readability
        plt.grid(True)
        plt.tight_layout()

        print("\nDisplaying Box Plot...")
        plt.show()
        print("\nDisplay closed")

    if n==6:
        break
