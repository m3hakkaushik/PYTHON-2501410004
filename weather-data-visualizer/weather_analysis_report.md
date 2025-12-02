# Weather Data Analysis Report

## Dataset Overview
- Total records analyzed: 137673
- Date range: 2007-11-01 to 2017-06-25
- Columns analyzed: Temperature, Rainfall, Humidity

## Key Findings

### Temperature Analysis
- Average Temperature: 17.69°C
- Minimum Temperature: -6.15°C
- Maximum Temperature: 38.80°C
- Temperature Variability (Std Dev): 6.26°C

The temperature data shows a range from -6.2°C to 38.8°C, 
indicating significant seasonal variation in the region.

### Rainfall Analysis
- Average Daily Rainfall: 2.33 mm
- Maximum Rainfall: 371.00 mm
- Total Rainfall Recorded: 320693.20 mm

The wettest month was Month 3 with 34568.70 mm total rainfall.
The driest month was Month 10 with 18483.80 mm total rainfall.

### Humidity Analysis
- Average Humidity: 60.10%
- Minimum Humidity: 0.00%
- Maximum Humidity: 100.00%

### Trends and Patterns
1. **Temperature-Humidity Relationship**: The scatter plot reveals a negative correlation between 
   temperature and humidity - higher temperatures tend to occur when humidity is lower.

2. **Seasonal Patterns**: The monthly rainfall chart shows clear wet and dry seasons, which is 
   typical for many Australian locations.

3. **Daily Variations**: Temperature shows consistent daily fluctuations throughout the year with 
   notable seasonal changes visible in the line chart.

## Conclusions
This analysis provides insights into local weather patterns that could be useful for:
- Campus sustainability planning
- Energy consumption forecasting
- Outdoor event scheduling
- Agricultural planning

## Files Generated
- cleaned_weather_data.csv: Cleaned dataset
- temperature_line_chart.png: Daily temperature trends
- rainfall_bar_chart.png: Monthly rainfall distribution
- humidity_temp_scatter.png: Humidity vs temperature relationship
- combined_plots.png: Combined visualization

## Tools Used
- Python 3.x
- Pandas: Data manipulation and cleaning
- NumPy: Statistical calculations
- Matplotlib: Data visualization

---
Report generated using Python data analysis tools.
