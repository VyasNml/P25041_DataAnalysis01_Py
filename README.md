**Project Title: Visualizing_Team_Standings Data Analytics Project** 

# 🔍 Overview

This project is a learning-based attempt to analyze and visualize sports standings data, with the goal of uncovering insights into team performance. The process helped in upskilling through hands-on experience with data analysis and visualization techniques.

# 🛠️ Technologies Used

• Python

• Pandas

• Matplotlib

• Seaborn

• Jupyter Notebook / VS Code

# 🎯 Objectives & Visual Insights

1️⃣ **Objective 1**: Analyze how team wins have changed across different seasons to identify performance trends.

**Description**: We analyze the top 3 teams per season based on points_differential, offering a clearer view of team dominance than win counts. The goal is to visualize how their performance shifts across seasons.

**Plot**: Line Plot

**Insight**: The plotted lines show point differential trends for the top 3 teams each season. Sharp changes indicate standout performances, while narrowing gaps suggest more competitive leagues, and wide gaps point to dominant teams.

2️⃣ **Objective 2**: Compare points scored versus points conceded to evaluate offensive and defensive strengths.

**Description**: We compute the average points scored (offense) and conceded (defense) by each team over all available seasons. A scatter plot is used to visualize the relationship between these metrics, providing a clearer comparison of team strengths.

**Plot**: Scatter Plot

**Insight**: The scatter plot reveals how teams perform offensively and defensively. Teams in the top-left corner show strong offense and defense, while teams in the bottom-right are weak in both areas.

3️⃣ **Objective 3**: Explore the distribution and variation of victory margins among teams.

**Description**: This objective analyzes the margin of victory (points_differential) across teams to understand how competitive or dominant the matches were. By examining these variations, we gain insights into team consistency and the overall level of competition.

**Plot**: Histogram

**Insight**: The histogram shows the frequency of specific victory margins. A concentration of low margins suggests close matches, indicating high league parity, while a spread toward larger margins points to one-sided contests. Peaks in specific bins highlight common score gaps.

4️⃣ **Objective 4**: Examine correlations between key performance metrics to discover influential factors.

**Description**: This objective uses correlation analysis to identify relationships between key performance metrics. A heatmap displays the correlation coefficients of selected numerical columns, making it easy to interpret how different factors are connected.

**Plot**: Heatmap

**Insight**: The heatmap reveals key relationships:

• A strong positive correlation between 'points_for' and 'wins', showing that scoring more leads to more victories.

• A strong negative correlation between 'points_against' and 'win_percentage', suggesting that conceding fewer points improves winning chances.

• A strong link between 'margin_of_victory' and 'win_percentage', indicating that higher victory margins are associated with better success metrics. These insights highlight the most influential statistics for overall performance.

5️⃣ **Objective 5**: Analyze distribution of points differential across teams.

**Description**: Box plots are used to visualize the distribution of points differential, highlighting average performance, consistency, and outliers across seasons.

**Plot**: Box Plot

**Insight**: Teams with higher medians and narrower IQRs show consistent strong performance. Outliers highlight standout or poor seasons.

# 📈 Key Learnings

• Hands-on practice with data cleaning, transformation, and visualization.

• Interpreting real-world sports data for analytical insights.

• Strengthened storytelling through visuals using Python libraries to effectively communicate complex patterns and trends.

# 🧠 Future Scope

- Add interactive dashboard using Plotly or Dash.

- Automate data updates via API integration for live sports data.

- Use machine learning to predict future rankings or outcomes.

# 🔗 References

- Python Documentation

- Pandas Official Docs

- Seaborn and Matplotlib Guides
Sports dataset (provided as part of coursework)
