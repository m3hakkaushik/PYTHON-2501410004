# Campus Energy-Use Dashboard
# This program analyzes electricity usage data from multiple buildings

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

print("=" * 60)
print("CAMPUS ENERGY DASHBOARD - STARTING ANALYSIS")
print("=" * 60)

# ===== TASK 3: OBJECT-ORIENTED MODELING =====
# Let's create our classes first (the building blocks of our program)

# This class represents a single meter reading
class MeterReading:
    """A single electricity meter reading with timestamp and usage"""
    
    def __init__(self, timestamp, kwh):
        # timestamp = when the reading was taken
        # kwh = how much electricity was used (kilowatt-hours)
        self.timestamp = timestamp
        self.kwh = kwh
    
    def __str__(self):
        # This lets us print the reading nicely
        return f"Reading on {self.timestamp}: {self.kwh} kWh"


# This class represents one building on campus
class Building:
    """Represents a campus building with its energy usage data"""
    
    def __init__(self, name):
        # name = building name (like "Library" or "Science Block")
        self.name = name
        self.meter_readings = []  # Empty list to store all readings
    
    def add_reading(self, timestamp, kwh):
        # Add a new meter reading to this building
        reading = MeterReading(timestamp, kwh)
        self.meter_readings.append(reading)
    
    def calculate_total_consumption(self):
        # Add up all the kWh from all readings
        total = 0
        for reading in self.meter_readings:
            total += reading.kwh
        return total
    
    def calculate_average_consumption(self):
        # Find the average usage
        if len(self.meter_readings) == 0:
            return 0
        total = self.calculate_total_consumption()
        return total / len(self.meter_readings)
    
    def calculate_min_consumption(self):
        # Find the lowest reading
        if len(self.meter_readings) == 0:
            return 0
        min_kwh = self.meter_readings[0].kwh
        for reading in self.meter_readings:
            if reading.kwh < min_kwh:
                min_kwh = reading.kwh
        return min_kwh
    
    def calculate_max_consumption(self):
        # Find the highest reading
        if len(self.meter_readings) == 0:
            return 0
        max_kwh = self.meter_readings[0].kwh
        for reading in self.meter_readings:
            if reading.kwh > max_kwh:
                max_kwh = reading.kwh
        return max_kwh
    
    def generate_report(self):
        # Create a text report for this building
        report = f"\n--- Report for {self.name} ---\n"
        report += f"Total Readings: {len(self.meter_readings)}\n"
        report += f"Total Consumption: {self.calculate_total_consumption():.2f} kWh\n"
        report += f"Average Consumption: {self.calculate_average_consumption():.2f} kWh\n"
        report += f"Minimum Reading: {self.calculate_min_consumption():.2f} kWh\n"
        report += f"Maximum Reading: {self.calculate_max_consumption():.2f} kWh\n"
        return report


# This class manages all buildings
class BuildingManager:
    """Manages all buildings on campus"""
    
    def __init__(self):
        # Dictionary to store buildings (key = name, value = Building object)
        self.buildings = {}
    
    def add_building(self, building_name):
        # Create a new building and add it to our collection
        if building_name not in self.buildings:
            self.buildings[building_name] = Building(building_name)
    
    def get_building(self, building_name):
        # Get a building by its name
        if building_name in self.buildings:
            return self.buildings[building_name]
        return None
    
    def get_all_buildings(self):
        # Return a list of all building names
        return list(self.buildings.keys())
    
    def get_total_campus_consumption(self):
        # Add up consumption from ALL buildings
        total = 0
        for building_name in self.buildings:
            building = self.buildings[building_name]
            total += building.calculate_total_consumption()
        return total
    
    def get_highest_consuming_building(self):
        # Find which building uses the most electricity
        highest_building = None
        highest_consumption = 0
        
        for building_name in self.buildings:
            building = self.buildings[building_name]
            consumption = building.calculate_total_consumption()
            if consumption > highest_consumption:
                highest_consumption = consumption
                highest_building = building_name
        
        return highest_building, highest_consumption


# ===== TASK 1: DATA INGESTION AND VALIDATION =====
print("\nTASK 1: Loading data from CSV files...")
print("-" * 60)

# Create a BuildingManager to manage all our buildings
manager = BuildingManager()

# This will store all data combined
all_data_list = []

# Check if data directory exists
data_dir = "data"
if not os.path.exists(data_dir):
    print(f"Creating '{data_dir}' directory...")
    os.makedirs(data_dir)
    print(f"⚠️  Please add your CSV files to the '{data_dir}' folder and run again!")
else:
    print(f"✓ Found '{data_dir}' directory")
    
    # Get all CSV files in the data directory
    csv_files = []
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            csv_files.append(filename)
    
    print(f"✓ Found {len(csv_files)} CSV file(s)")
    
    # Load each CSV file
    for filename in csv_files:
        filepath = os.path.join(data_dir, filename)
        print(f"\nLoading: {filename}")
        
        try:
            # Try to read the CSV file
            df = pd.read_csv(filepath, on_bad_lines='skip')
            
            # Extract building name from filename (remove .csv extension)
            building_name = filename.replace('.csv', '')
            
            # Add building to manager
            manager.add_building(building_name)
            building = manager.get_building(building_name)
            
            # Make sure the CSV has the columns we need
            if 'Date' in df.columns and 'kWh' in df.columns:
                # Convert date column to datetime
                df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
                
                # Add building name column if not present
                df['Building'] = building_name
                
                # Add each reading to the building object
                for index, row in df.iterrows():
                    if pd.notna(row['Date']) and pd.notna(row['kWh']):
                        building.add_reading(row['Date'], row['kWh'])
                
                # Add to our combined list
                all_data_list.append(df)
                
                print(f"  ✓ Loaded {len(df)} records from {building_name}")
            else:
                print(f"  ⚠️  Missing required columns (Date, kWh) in {filename}")
                
        except FileNotFoundError:
            print(f"  ✗ File not found: {filename}")
        except Exception as e:
            print(f"  ✗ Error reading {filename}: {str(e)}")

# Combine all DataFrames into one
if len(all_data_list) > 0:
    df_combined = pd.concat(all_data_list, ignore_index=True)
    print(f"\n✓ Combined dataset has {len(df_combined)} total records")
    print(f"✓ Tracking {len(manager.get_all_buildings())} buildings")
else:
    print("\n⚠️  No data loaded! Please add CSV files to the data folder.")
    print("   Each CSV should have 'Date' and 'kWh' columns")
    df_combined = pd.DataFrame()  # Empty dataframe


# ===== TASK 2: CORE AGGREGATION LOGIC =====
print("\n" + "=" * 60)
print("TASK 2: Calculating statistics and aggregations...")
print("-" * 60)

# Function to calculate daily totals
def calculate_daily_totals(df):
    """Calculate total kWh for each day"""
    if df.empty:
        return pd.DataFrame()
    
    # Group by date and sum the kWh
    df['Date'] = pd.to_datetime(df['Date'])
    daily = df.groupby(df['Date'].dt.date)['kWh'].sum().reset_index()
    daily.columns = ['Date', 'Total_kWh']
    return daily

# Function to calculate weekly aggregates
def calculate_weekly_aggregates(df):
    """Calculate weekly totals and averages"""
    if df.empty:
        return pd.DataFrame()
    
    # Set date as index for resampling
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    df_copy = df_copy.set_index('Date')
    
    # Resample by week ('W') and calculate sum
    weekly = df_copy['kWh'].resample('W').sum().reset_index()
    weekly.columns = ['Week', 'Total_kWh']
    return weekly

# Function to create building-wise summary
def building_wise_summary(df):
    """Create summary statistics for each building"""
    if df.empty:
        return {}
    
    summary = {}
    buildings = df['Building'].unique()
    
    for building in buildings:
        building_data = df[df['Building'] == building]
        summary[building] = {
            'mean': building_data['kWh'].mean(),
            'min': building_data['kWh'].min(),
            'max': building_data['kWh'].max(),
            'total': building_data['kWh'].sum(),
            'count': len(building_data)
        }
    
    return summary

# Calculate aggregations
if not df_combined.empty:
    daily_totals = calculate_daily_totals(df_combined)
    weekly_totals = calculate_weekly_aggregates(df_combined)
    building_summary = building_wise_summary(df_combined)
    
    print("\n✓ Daily totals calculated")
    print(f"  Total days: {len(daily_totals)}")
    
    print("\n✓ Weekly totals calculated")
    print(f"  Total weeks: {len(weekly_totals)}")
    
    print("\n✓ Building-wise summary:")
    for building_name, stats in building_summary.items():
        print(f"  {building_name}:")
        print(f"    Average: {stats['mean']:.2f} kWh")
        print(f"    Min: {stats['min']:.2f} kWh")
        print(f"    Max: {stats['max']:.2f} kWh")
        print(f"    Total: {stats['total']:.2f} kWh")
else:
    daily_totals = pd.DataFrame()
    weekly_totals = pd.DataFrame()
    building_summary = {}
    print("⚠️  No data to aggregate")


# ===== TASK 4: VISUAL OUTPUT WITH MATPLOTLIB =====
print("\n" + "=" * 60)
print("TASK 4: Creating visualizations...")
print("-" * 60)

if not df_combined.empty and len(manager.get_all_buildings()) > 0:
    # Create a figure with 3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 14))
    fig.suptitle('Campus Energy Consumption Dashboard', fontsize=16, fontweight='bold')
    
    # PLOT 1: Daily consumption trend line
    if not daily_totals.empty:
        daily_totals['Date'] = pd.to_datetime(daily_totals['Date'])
        ax1.plot(daily_totals['Date'], daily_totals['Total_kWh'], 
                 color='blue', linewidth=2, marker='o', markersize=3)
        ax1.set_xlabel('Date', fontsize=10)
        ax1.set_ylabel('Total Energy (kWh)', fontsize=10)
        ax1.set_title('Daily Energy Consumption Over Time', fontsize=12, fontweight='bold')
        ax1.grid(True, alpha=0.3)
        ax1.tick_params(axis='x', rotation=45)
    
    # PLOT 2: Bar chart comparing average weekly usage across buildings
    if building_summary:
        buildings = list(building_summary.keys())
        averages = [building_summary[b]['mean'] for b in buildings]
        
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        ax2.bar(buildings, averages, color=colors[:len(buildings)], alpha=0.7, edgecolor='black')
        ax2.set_xlabel('Building', fontsize=10)
        ax2.set_ylabel('Average kWh', fontsize=10)
        ax2.set_title('Average Energy Usage by Building', fontsize=12, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='y')
        ax2.tick_params(axis='x', rotation=45)
    
    # PLOT 3: Scatter plot - peak hour consumption
    if not df_combined.empty:
        # Add hour column if we have time data
        df_combined['Hour'] = pd.to_datetime(df_combined['Date']).dt.hour
        
        # Create scatter plot with different color for each building
        buildings = df_combined['Building'].unique()
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
        
        for i, building in enumerate(buildings):
            building_data = df_combined[df_combined['Building'] == building]
            ax3.scatter(building_data['Date'], building_data['kWh'], 
                       label=building, alpha=0.6, s=50, 
                       color=colors[i % len(colors)])
        
        ax3.set_xlabel('Date', fontsize=10)
        ax3.set_ylabel('Energy Usage (kWh)', fontsize=10)
        ax3.set_title('Energy Consumption Pattern by Building', fontsize=12, fontweight='bold')
        ax3.legend(loc='best', fontsize=8)
        ax3.grid(True, alpha=0.3)
        ax3.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig('dashboard.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: dashboard.png")
    plt.close()
else:
    print("⚠️  Not enough data to create visualizations")


# ===== TASK 5: PERSISTENCE AND EXECUTIVE SUMMARY =====
print("\n" + "=" * 60)
print("TASK 5: Exporting data and generating summary...")
print("-" * 60)

# Create output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Export cleaned data
if not df_combined.empty:
    df_combined.to_csv('output/cleaned_energy_data.csv', index=False)
    print("✓ Saved: output/cleaned_energy_data.csv")

# Export building summary as CSV
if building_summary:
    summary_df = pd.DataFrame.from_dict(building_summary, orient='index')
    summary_df.to_csv('output/building_summary.csv')
    print("✓ Saved: output/building_summary.csv")

# Generate executive summary report
summary_text = "=" * 60 + "\n"
summary_text += "CAMPUS ENERGY CONSUMPTION - EXECUTIVE SUMMARY\n"
summary_text += "=" * 60 + "\n\n"

if not df_combined.empty:
    # Total campus consumption
    total_consumption = manager.get_total_campus_consumption()
    summary_text += f"TOTAL CAMPUS CONSUMPTION: {total_consumption:,.2f} kWh\n\n"
    
    # Highest consuming building
    highest_building, highest_consumption = manager.get_highest_consuming_building()
    summary_text += f"HIGHEST CONSUMING BUILDING:\n"
    summary_text += f"  {highest_building}: {highest_consumption:,.2f} kWh\n\n"
    
    # Peak load information
    if not df_combined.empty:
        peak_row = df_combined.loc[df_combined['kWh'].idxmax()]
        summary_text += f"PEAK LOAD:\n"
        summary_text += f"  Time: {peak_row['Date']}\n"
        summary_text += f"  Building: {peak_row['Building']}\n"
        summary_text += f"  Usage: {peak_row['kWh']:.2f} kWh\n\n"
    
    # Daily and weekly trends
    if not daily_totals.empty:
        avg_daily = daily_totals['Total_kWh'].mean()
        summary_text += f"DAILY TRENDS:\n"
        summary_text += f"  Average daily consumption: {avg_daily:.2f} kWh\n"
        summary_text += f"  Highest daily total: {daily_totals['Total_kWh'].max():.2f} kWh\n"
        summary_text += f"  Lowest daily total: {daily_totals['Total_kWh'].min():.2f} kWh\n\n"
    
    if not weekly_totals.empty:
        avg_weekly = weekly_totals['Total_kWh'].mean()
        summary_text += f"WEEKLY TRENDS:\n"
        summary_text += f"  Average weekly consumption: {avg_weekly:.2f} kWh\n"
        summary_text += f"  Highest weekly total: {weekly_totals['Total_kWh'].max():.2f} kWh\n\n"
    
    # Building-by-building breakdown
    summary_text += "BUILDING-BY-BUILDING BREAKDOWN:\n"
    summary_text += "-" * 60 + "\n"
    for building_name in manager.get_all_buildings():
        building = manager.get_building(building_name)
        summary_text += building.generate_report()
    
    summary_text += "\n" + "=" * 60 + "\n"
    summary_text += "RECOMMENDATIONS:\n"
    summary_text += "- Focus energy-saving initiatives on high-consumption buildings\n"
    summary_text += "- Monitor peak usage times for load management\n"
    summary_text += "- Consider renewable energy sources for major consumers\n"
    summary_text += "- Implement automated monitoring systems\n"
    summary_text += "=" * 60 + "\n"
else:
    summary_text += "No data available for analysis.\n"
    summary_text += "Please add CSV files to the 'data' directory.\n"

# Save summary to file
with open('output/summary.txt', 'w') as f:
    f.write(summary_text)

print("✓ Saved: output/summary.txt")

# Print summary to console
print("\n" + "=" * 60)
print("EXECUTIVE SUMMARY")
print("=" * 60)
print(summary_text)

print("\n" + "=" * 60)
print("✅ ANALYSIS COMPLETE!")
print("=" * 60)
print("\nGenerated files:")
print("  1. output/cleaned_energy_data.csv")
print("  2. output/building_summary.csv")
print("  3. output/summary.txt")
print("  4. dashboard.png")
print("\nReady to upload to GitHub!")