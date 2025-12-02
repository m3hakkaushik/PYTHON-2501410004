# Weather Data Visualizer

## Project Overview

This project analyzes Australian weather data to identify patterns and trends in temperature, rainfall, and humidity. The analysis includes statistical computations and data visualizations that help understand climate patterns.

## Terminal

<img width="950" height="437" alt="Screenshot 2025-12-02 at 3 47 39 PM" src="https://github.com/user-attachments/assets/533c30e8-775a-44f2-9cb3-b21511bc3672" />

## Dataset Description
1. **Source:** weatherAUS.csv (Australian weather dataset)
2. **Columns Used:**
   1. Date: Date of observation
   2. MinTemp: Minimum temperature (°C)
   3. MaxTemp: Maximum temperature (°C)
   4. Rainfall: Rainfall amount (mm)
   5. Humidity9am: Morning humidity (%)
   6. Humidity3pm: Afternoon humidity (%)
3. **Tools and Libraries Used:**
   1. **Python 3.x:** Programming language
   2. **Pandas:** Data loading, cleaning, and manipulation
   3. **NumPy:** Statistical calculations (mean, min, max, standard deviation)
   4. **Matplotlib:** Creating charts and visualizations
   
## Installation Instructions

1. Make sure you have Python installed
2. Install required libraries:
   ``pip install pandas numpy matplotlib``
3. Download the weatherAUS.csv file
4. Run the script:
   ``python weather_visualizer.py``
   
## Analysis Process

1. **Data Loading**
Loaded the CSV file and inspected the structure to understand the data.

2. **Data Cleaning**
   1.Converted date strings to datetime format
   2. Removed rows with missing values
   3. Selected relevant columns for analysis
   4. Created calculated columns (average temperature, average humidity)

3. **Statistical Analysis**
Computed key statistics using NumPy:
   1. Mean, minimum, maximum temperatures
   2. Rainfall totals and averages
   3. Humidity variations
   
4. **Data Visualization**
Created four charts:
   1. Line Chart: Daily temperature trends over time
   2. Bar Chart: Monthly rainfall totals
   3. Scatter Plot: Relationship between humidity and temperature
   4. Combined Plot: Temperature and rainfall in one figure
   
6. **Grouping and Aggregation**
Grouped data by month to identify seasonal patterns in:
   1. Temperature variations
   2. Rainfall distribution
   3. Humidity levels
   
## Results and Insights

<img width="217" height="129" alt="image" src="https://github.com/user-attachments/assets/f3538d20-9cff-414f-bf0c-b5b50e13245e" />


**Key Findings:**

   1. **Temperature:** Wide variation showing clear seasonal patterns
   
   2. **Rainfall:** Distinct wet and dry months identified
   
   3. **Humidity-Temperature Relationship:** Inverse correlation observed - higher temperatures typically occur with lower humidity

   
**Generated Files:**

   1. ``cleaned_weather_data.csv``: Cleaned dataset ready for further analysis
   
   2. ``temperature_line_chart.png``: Visual of temperature trends
   
   3. ``rainfall_bar_chart.png``: Monthly rainfall comparison
   
   4. ``humidity_temp_scatter.png``: Humidity vs temperature relationship
   
   5. ``combined_plots.png``: Multiple visualizations in one figure
   
   6. ``weather_analysis_report.md``: Detailed analysis summary
   
## Applications

This analysis could be useful for:

   1. Campus sustainability initiatives
   
   2. Energy consumption planning
   
   3. Agricultural decision-making
   
   4. Outdoor event scheduling
   
   
## Project Structure

<img width="576" height="296" alt="Screenshot 2025-12-02 at 4 05 36 PM" src="https://github.com/user-attachments/assets/374da019-bc3f-4e6f-a4a2-1c16908d5e17" />


  
## How to Use
1. Clone this repository 
2. Ensure all required libraries are installed
3. Place the *weatherAUS.csv* file in the same directory
4. Run ``python weather_visualizer.py``
5. Check the output files and visualizations
   
## Author

Mehak
Lasted Date : December 2025

## Acknowledgments

   1. Dataset source: Australian weather data
   2. Course: Programming for Problem Solving using Python
   3. Assignment: Weather Data Visualizer Mini Project
