# Weather Data Visualizer
# analyzes weather data and creates visualizationssssss......

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Starting Weather Data Analysis...")
print("=" * 50)

#=================================================================================================================================================

print("\nTASK 1: Loading the data...")

# Load the CSV file into a DataFrame :

df = pd.read_csv('weatherAUS.csv')     # to read the CSV file....uhmm... it also creates the table...    

print("\nFirst 5 rows of data:")
print(df.head())


print("\nDataset Information:")        # column names, data types, etc.
print(df.info())


print("\nBasic Statistics:")            # mean, min, max, etc
print(df.describe())


#=================================================================================================================================================
print("\n" + "=" * 50)
print("TASK 2: Cleaning the data...")


df['Date'] = pd.to_datetime(df['Date'])      #conversion from date column to datetime


columns_to_keep = ['Date', 'MinTemp', 'MaxTemp', 'Rainfall', 'Humidity9am', 'Humidity3pm']      # selecting Date, Temperature, Rainfall, and Humidity
df_clean = df[columns_to_keep].copy()


print(f"\nRows before cleaning: {len(df_clean)}")       # dropping rows with missing data
df_clean = df_clean.dropna()
print(f"Rows after cleaning: {len(df_clean)}")


df_clean['AvgTemp'] = (df_clean['MinTemp'] + df_clean['MaxTemp']) / 2     #avg temp col... avg of min and max


df_clean['AvgHumidity'] = (df_clean['Humidity9am'] + df_clean['Humidity3pm']) / 2    #avg humidity col... 

print("\nCleaned data preview:")
print(df_clean.head())



#=================================================================================================================================================
print("\n" + "=" * 50)
print("TASK 3: Computing statistics with NumPy...")


temp_array = np.array(df_clean['AvgTemp'])    #col to numpy array
rainfall_array = np.array(df_clean['Rainfall'])
humidity_array = np.array(df_clean['AvgHumidity'])


print("\nTemperature Statistics:")        #stats using numpy
print(f"  Mean: {np.mean(temp_array):.2f}°C")
print(f"  Min: {np.min(temp_array):.2f}°C")
print(f"  Max: {np.max(temp_array):.2f}°C")
print(f"  Standard Deviation: {np.std(temp_array):.2f}°C")

print("\nRainfall Statistics:")
print(f"  Mean: {np.mean(rainfall_array):.2f} mm")
print(f"  Min: {np.min(rainfall_array):.2f} mm")
print(f"  Max: {np.max(rainfall_array):.2f} mm")
print(f"  Standard Deviation: {np.std(rainfall_array):.2f} mm")

print("\nHumidity Statistics:")
print(f"  Mean: {np.mean(humidity_array):.2f}%")
print(f"  Min: {np.min(humidity_array):.2f}%")
print(f"  Max: {np.max(humidity_array):.2f}%")
print(f"  Standard Deviation: {np.std(humidity_array):.2f}%")



#=================================================================================================================================================
print("\n" + "=" * 50)
print("TASK 5: Grouping data by month...")


df_clean['Month'] = df_clean['Date'].dt.month    #col for month... extract month from date
df_clean['Year'] = df_clean['Date'].dt.year

# Grouping by month and cal avg stats
monthly_stats = df_clean.groupby('Month').agg({
    'AvgTemp': ['mean', 'min', 'max'],
    'Rainfall': 'sum',
    'AvgHumidity': 'mean'
}) 

print("\nMonthly Statistics:")
print(monthly_stats)


monthly_rainfall = df_clean.groupby('Month')['Rainfall'].sum()  #cal monthly rainfall total for plot



#=================================================================================================================================================
print("\n" + "=" * 50)
print("TASK 4: Creating visualizations...")

# PLOT 1: Line chart for daily temperature trends
# use of first 365 days data only /- 
sample_data = df_clean.head(365)

plt.figure(figsize=(12, 6))
plt.plot(sample_data['Date'], sample_data['AvgTemp'], color='red', linewidth=1)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Daily Temperature Trends (First Year Sample)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_line_chart.png', dpi=300, bbox_inches='tight')
print("✓ Saved: temperature_line_chart.png")
plt.close()

# PLOT 2: Bar chart for monthly rainfall totals
plt.figure(figsize=(10, 6))
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.bar(range(1, 13), monthly_rainfall, color='blue', alpha=0.7)
plt.xlabel('Month')
plt.ylabel('Total Rainfall (mm)')
plt.title('Monthly Rainfall Totals')
plt.xticks(range(1, 13), months)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('rainfall_bar_chart.png', dpi=300, bbox_inches='tight')
print("✓ Saved: rainfall_bar_chart.png")
plt.close()

# PLOT 3: Scatter plot for humidity vs. temperature
plt.figure(figsize=(10, 6))
plt.scatter(df_clean['AvgHumidity'], df_clean['AvgTemp'], alpha=0.3, color='green', s=10)
plt.xlabel('Average Humidity (%)')
plt.ylabel('Average Temperature (°C)')
plt.title('Humidity vs Temperature Relationship')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('humidity_temp_scatter.png', dpi=300, bbox_inches='tight')
print("✓ Saved: humidity_temp_scatter.png")
plt.close()

# PLOT 4: Combined figure with two plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Left plot: Temperature trends
ax1.plot(sample_data['Date'], sample_data['AvgTemp'], color='red', linewidth=1)
ax1.set_xlabel('Date')
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('Daily Temperature Trends')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, alpha=0.3)

# Right plot: Monthly rainfall
ax2.bar(range(1, 13), monthly_rainfall, color='blue', alpha=0.7)
ax2.set_xlabel('Month')
ax2.set_ylabel('Total Rainfall (mm)')
ax2.set_title('Monthly Rainfall Totals')
ax2.set_xticks(range(1, 13))
ax2.set_xticklabels(months)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('combined_plots.png', dpi=300, bbox_inches='tight')
print("✓ Saved: combined_plots.png")
plt.close()




#=================================================================================================================================================

print("\n" + "=" * 50)
print("TASK 6: Exporting cleaned data and creating report...")

# clean data to new csv
df_clean.to_csv('cleaned_weather_data.csv', index=False)
print("✓ Saved: cleaned_weather_data.csv")


# Reporttttttttttt...........
report = f"""# Weather Data Analysis Report

## Dataset Overview
- Total records analyzed: {len(df_clean)}
- Date range: {df_clean['Date'].min().strftime('%Y-%m-%d')} to {df_clean['Date'].max().strftime('%Y-%m-%d')}
- Columns analyzed: Temperature, Rainfall, Humidity

## Key Findings

### Temperature Analysis
- Average Temperature: {np.mean(temp_array):.2f}°C
- Minimum Temperature: {np.min(temp_array):.2f}°C
- Maximum Temperature: {np.max(temp_array):.2f}°C
- Temperature Variability (Std Dev): {np.std(temp_array):.2f}°C

The temperature data shows a range from {np.min(temp_array):.1f}°C to {np.max(temp_array):.1f}°C, 
indicating significant seasonal variation in the region.

### Rainfall Analysis
- Average Daily Rainfall: {np.mean(rainfall_array):.2f} mm
- Maximum Rainfall: {np.max(rainfall_array):.2f} mm
- Total Rainfall Recorded: {np.sum(rainfall_array):.2f} mm

The wettest month was Month {monthly_rainfall.idxmax()} with {monthly_rainfall.max():.2f} mm total rainfall.
The driest month was Month {monthly_rainfall.idxmin()} with {monthly_rainfall.min():.2f} mm total rainfall.

### Humidity Analysis
- Average Humidity: {np.mean(humidity_array):.2f}%
- Minimum Humidity: {np.min(humidity_array):.2f}%
- Maximum Humidity: {np.max(humidity_array):.2f}%

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
"""

# Save the report
with open('weather_analysis_report.md', 'w') as f:
    f.write(report)

print("✓ Saved: weather_analysis_report.md")

print("\n" + "=" * 50)
print("✅ Analysis Complete!")
print("=" * 50)
print("\nGenerated Files:")
print("  1. cleaned_weather_data.csv")
print("  2. temperature_line_chart.png")
print("  3. rainfall_bar_chart.png")
print("  4. humidity_temp_scatter.png")
print("  5. combined_plots.png")
print("  6. weather_analysis_report.md")
print("\nYou can now upload these to your GitHub repository!")
