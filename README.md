# Hospital Operations Analysis

## Project Overview

This project analyzes hospital scheduling data to identify patterns in appointment wait times and operational efficiency.

## Objective

The goal is to evaluate:
- Appointment delays
- High-volume scheduling periods
- Operational bottlenecks
- Factors associated with longer wait times

## Tools Used

- Python
- Pandas
- Matplotlib
- Excel

## Dataset

Hospital appointment scheduling dataset containing 42,766 records.

The raw dataset is not included due to data-sharing limitations.

## Data Analysis

Completed:
- Data quality checks
- Missing value analysis
- Duplicate record checks
- Delay classification
- Time-based analysis
- Appointment volume analysis

## Key Findings

- Identified hours with higher average delays.
- Compared appointment volume with delay frequency.
- Evaluated operational patterns throughout the day.

## Future Improvements

- Create an interactive dashboard using Power BI or Streamlit.
- Add predictive modeling for wait-time forecasting.
- Integrate SQL database analysis.

# NBA Player Analytics Project 🏀

## Overview

This project analyzes NBA player performance data using Python and the NBA API. The goal is to explore relationships between player statistics, identify performance trends, and develop a foundation for creating data-driven player evaluation models.

The project follows a complete data analytics workflow:
- Data collection through an API
- Data cleaning and organization
- Exploratory data analysis
- Statistical analysis
- Data visualization

---

## Research Question

**Which player statistics are most strongly associated with NBA scoring performance?**

This project explores how statistics such as minutes played, field goal attempts, rebounds, assists, and other performance metrics relate to total points scored.

---

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- NBA API
- Git/GitHub

---

## Project Structure
NBA-Player-Analytics/
├── data/
│ └── player_stats.csv
├── graphs/
│ ├── points_distribution.png
│ ├── minutes_vs_points.png
│ ├── top_scorers.png
│ ├── rebounds_vs_blocks.png
│ └── correlation_heatmap.png
├── script/
│ ├── get_players.py
│ ├── player_stats.py
│ ├── eda.py
│ ├── visualizations.py
│ └── correlation.py
└── README.md

---

## Data Collection

Player information was collected using the NBA API.

The project first retrieves NBA player identifiers and then uses those IDs to collect career statistics including:

- Games Played (GP)
- Minutes Played (MIN)
- Points (PTS)
- Rebounds (REB)
- Assists (AST)
- Steals (STL)
- Blocks (BLK)
- Shooting statistics

---

## Exploratory Data Analysis

Initial analysis included:

- Reviewing dataset structure and summary statistics
- Identifying highest scoring players
- Finding statistical averages
- Examining player performance distributions

Example questions explored:

- Who are the highest scoring player-seasons?
- What statistics are most common among NBA players?
- How does playing time relate to scoring output?

---

## Visualizations

Created visualizations to explore player performance relationships:

### Minutes Played vs Points Scored

Examines whether players with more playing time tend to produce more points.

### Top 10 Highest Scoring Seasons

Highlights player-seasons with the highest total scoring output.

### Assists vs Turnovers

Explores the relationship between playmaking and ball control.

### Rebounds vs Blocks

Analyzes defensive and rebounding performance relationships.

---

## Correlation Analysis

Correlation analysis was performed to identify which statistics have the strongest relationship with scoring.

Key variables analyzed:

- Minutes Played
- Field Goal Attempts
- Field Goals Made
- Assists
- Rebounds
- Defensive statistics

---

## Future Improvements

Future development of this project includes:

- Creating a custom player evaluation score
- Comparing players across seasons
- Building a machine learning model to predict player performance
- Developing an interactive dashboard using Streamlit

---

## Author

Aaliyah Martin  
Mathematics Undergraduate | Mathematical Analysis & Operations Research  
Interested in Data Analytics, Sports Analytics, and Operations Research
