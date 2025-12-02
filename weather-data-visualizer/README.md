## Weather Data Visualizer

# Project Overview

This project analyzes Australian weather data to identify patterns and trends in temperature, rainfall, and humidity. The analysis includes statistical computations and data visualizations that help understand climate patterns.


# Dataset Description
1. Source: weatherAUS.csv (Australian weather dataset)
2. Columns Used:
   ~ Date: Date of observation
   ~ MinTemp: Minimum temperature (°C)
   ~ MaxTemp: Maximum temperature (°C)
   ~ Rainfall: Rainfall amount (mm)
   ~ Humidity9am: Morning humidity (%)
   ~ Humidity3pm: Afternoon humidity (%)
3. Tools and Libraries Used
   ~ Python 3.x: Programming language
   ~ Pandas: Data loading, cleaning, and manipulation
   ~ NumPy: Statistical calculations (mean, min, max, standard deviation)
   ~ Matplotlib: Creating charts and visualizations
   
# Installation Instructions

1. Make sure you have Python installed
2. Install required libraries:
   ~ pip install pandas numpy matplotlib
3. Download the weatherAUS.csv file
4. Run the script:
   ~ python weather_visualizer.py
   
# Analysis Process

1. Data Loading
Loaded the CSV file and inspected the structure to understand the data.

2. Data Cleaning
Converted date strings to datetime format
Removed rows with missing values
Selected relevant columns for analysis
Created calculated columns (average temperature, average humidity)

4. Statistical Analysis
Computed key statistics using NumPy:
   ~ Mean, minimum, maximum temperatures
   ~ Rainfall totals and averages
   ~ Humidity variations
   
4. Data Visualization
Created four charts:
   ~ Line Chart: Daily temperature trends over time
   ~ Bar Chart: Monthly rainfall totals
   ~ Scatter Plot: Relationship between humidity and temperature
   ~ Combined Plot: Temperature and rainfall in one figure
   
6. Grouping and Aggregation
Grouped data by month to identify seasonal patterns in:
   ~ Temperature variations
   ~ Rainfall distribution
   ~ Humidity levels
   
# Results and Insights

Key Findings:
   ~ Temperature: Wide variation showing clear seasonal patterns
   ~ Rainfall: Distinct wet and dry months identified
   ~ Humidity-Temperature Relationship: Inverse correlation observed - higher temperatures typically occur with lower humidity
Generated Files:
   ~ cleaned_weather_data.csv: Cleaned dataset ready for further analysis
   ~ temperature_line_chart.png: Visual of temperature trends
   ~ rainfall_bar_chart.png: Monthly rainfall comparison
   ~ humidity_temp_scatter.png: Humidity vs temperature relationship
   ~ combined_plots.png: Multiple visualizations in one figure
   ~ weather_analysis_report.md: Detailed analysis summary
   
# Applications

This analysis could be useful for:
   ~ Campus sustainability initiatives
   ~ Energy consumption planning
   ~ Agricultural decision-making
   ~ Outdoor event scheduling
   
# Project Structure

weather-data-visualizer/
│
├── weather_visualizer.py          # Main analysis script
├── weatherAUS.csv                 # Original dataset
├── cleaned_weather_data.csv       # Cleaned dataset
├── README.md                      # This file
├── weather_analysis_report.md     # Detailed findings
│
└── visualizations/
    ├── temperature_line_chart.png
    ├── rainfall_bar_chart.png
    ├── humidity_temp_scatter.png
    └── combined_plots.png
    
# How to Use
1. Clone this repository
2. Ensure all required libraries are installed
3. Place the weatherAUS.csv file in the same directory
4. Run python weather_visualizer.py
5. Check the output files and visualizations
   
# Author

Mehak
Lasted Date : December 2025

# Acknowledgments

   ~ Dataset source: Australian weather data
   ~ Course: Programming for Problem Solving using Python
   ~ Assignment: Weather Data Visualizer Mini Project
