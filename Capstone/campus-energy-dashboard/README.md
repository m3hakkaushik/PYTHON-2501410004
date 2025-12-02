Campus Energy-Use Dashboard
Project Overview
This capstone project analyzes electricity consumption data from multiple campus buildings to identify energy-saving opportunities. The system automatically reads meter data, performs statistical analysis, and generates visual dashboards to support administrative decision-making.

Real-World Application
The campus facilities team can use this dashboard to:

Identify high-consumption buildings for targeted energy-saving initiatives
Monitor daily and weekly usage patterns
Detect unusual spikes in energy consumption
Plan renewable energy installations based on usage data
Make informed decisions about building operations
Dataset Description
The project processes multiple CSV files, each representing a building's monthly meter readings:

Required CSV Format:

Date: Date of meter reading (YYYY-MM-DD format)
kWh: Energy consumption in kilowatt-hours
Sample Buildings:

Library
Science Block
Admin Building
Cafeteria
Sports Complex
Each CSV file should be named after the building (e.g., Library.csv, Science_Block.csv)

Tools and Libraries Used
Python 3.x: Core programming language
Pandas: Data loading, cleaning, and aggregation
Matplotlib: Creating visualizations and charts
NumPy: Numerical calculations
os/pathlib: File system operations
datetime: Date and time handling
Installation Instructions
1. Prerequisites
Make sure you have Python 3.x installed on your computer.

2. Install Required Libraries
bash
pip install pandas matplotlib numpy
3. Project Setup
bash
# Clone the repository
git clone https://github.com/yourusername/campus-energy-dashboard-yourname.git
cd campus-energy-dashboard-yourname

# Project structure will be created automatically
How to Use
Step 1: Generate Sample Data (For Testing)
If you don't have real data yet, run the sample data generator:

bash
python generate_sample_data.py
This creates a data/ folder with sample CSV files for 5 buildings.

Step 2: Run the Main Analysis
bash
python energy_dashboard.py
Step 3: Check the Output
The program will create:

output/cleaned_energy_data.csv - All building data combined and cleaned
output/building_summary.csv - Statistical summary for each building
output/summary.txt - Executive summary report
dashboard.png - Visual dashboard with 3 charts
Project Architecture
Object-Oriented Design
1. MeterReading Class
Represents a single electricity meter reading.

Stores timestamp and kWh value
Provides string representation for debugging
2. Building Class
Represents a campus building with all its meter readings.

Attributes:

name: Building name
meter_readings: List of MeterReading objects
Methods:

add_reading(): Add a new meter reading
calculate_total_consumption(): Sum all readings
calculate_average_consumption(): Calculate mean usage
calculate_min_consumption(): Find minimum reading
calculate_max_consumption(): Find maximum reading
generate_report(): Create text summary
3. BuildingManager Class
Manages all buildings on campus.

Attributes:

buildings: Dictionary of Building objects
Methods:

add_building(): Register a new building
get_building(): Retrieve building by name
get_all_buildings(): List all building names
get_total_campus_consumption(): Calculate campus-wide total
get_highest_consuming_building(): Identify top consumer
Core Functions
Data Aggregation Functions
calculate_daily_totals(df)

Groups data by date
Sums kWh for each day
Returns DataFrame with daily totals
calculate_weekly_aggregates(df)

Uses Pandas resample to group by week
Calculates weekly consumption totals
Useful for identifying weekly patterns
building_wise_summary(df)

Creates dictionary with statistics per building
Calculates mean, min, max, and total for each building
Returns structured summary data
Features Implemented
Task 1: Data Ingestion and Validation ✓
Automatically scans data/ directory for CSV files
Handles missing files with try-except blocks
Skips corrupt data lines
Logs loading status for each file
Combines all files into single DataFrame
Task 2: Core Aggregation Logic ✓
Daily consumption totals
Weekly aggregated statistics
Building-wise summaries with mean, min, max, total
Uses groupby and resample operations
Task 3: Object-Oriented Modeling ✓
MeterReading class for individual readings
Building class with consumption methods
BuildingManager class for campus-wide operations
Clear separation of concerns
Task 4: Visual Output with Matplotlib ✓
Creates dashboard with 3 visualizations:

Trend Line Chart: Daily consumption over time for all buildings
Bar Chart: Average weekly usage comparison across buildings
Scatter Plot: Consumption patterns by building and time
All charts combined in single PNG with proper labels and legends.

Task 5: Persistence and Executive Summary ✓
Exports:

Cleaned dataset (CSV)
Building summary statistics (CSV)
Executive summary report (TXT)
Report includes:

Total campus consumption
Highest-consuming building
Peak load time and location
Daily and weekly trends
Building-by-building breakdown
Recommendations for energy saving
Output Examples
Console Output
TASK 1: Loading data from CSV files...
✓ Found 'data' directory
✓ Found 5 CSV file(s)

Loading: Library.csv
  ✓ Loaded 90 records from Library

TASK 2: Calculating statistics and aggregations...
✓ Building-wise summary:
  Library:
    Average: 148.52 kWh
    Total: 13,366.80 kWh
Dashboard Visualization
The dashboard.png contains:

Top: Line chart showing daily trends
Middle: Bar chart comparing buildings
Bottom: Scatter plot of consumption patterns
Executive Summary (summary.txt)
TOTAL CAMPUS CONSUMPTION: 67,845.23 kWh

HIGHEST CONSUMING BUILDING:
  Science_Block: 24,532.10 kWh

RECOMMENDATIONS:
- Focus energy-saving initiatives on high-consumption buildings
- Monitor peak usage times for load management
Error Handling
The program includes robust error handling:

FileNotFoundError: Gracefully handles missing CSV files
Corrupt Data: Skips bad lines using on_bad_lines='skip'
Missing Columns: Validates required columns exist
Empty Data: Checks for empty DataFrames before processing
Date Parsing: Uses errors='coerce' for invalid dates
File Structure
campus-energy-dashboard/
│
├── energy_dashboard.py           # Main analysis script
├── generate_sample_data.py       # Sample data generator (for testing)
├── README.md                      # This file
│
├── data/                          # Input data folder
│   ├── Library.csv
│   ├── Science_Block.csv
│   ├── Admin_Building.csv
│   ├── Cafeteria.csv
│   └── Sports_Complex.csv
│
├── output/                        # Generated output
│   ├── cleaned_energy_data.csv
│   ├── building_summary.csv
│   └── summary.txt
│
└── dashboard.png                  # Visual dashboard
Methodology
Data Processing Pipeline
Ingestion: Load all CSV files from data directory
Validation: Check for required columns and valid data
Cleaning: Remove missing values, convert dates
Object Creation: Build Building objects with readings
Aggregation: Calculate daily, weekly, and building stats
Visualization: Create multi-chart dashboard
Export: Save cleaned data, summaries, and reports
Statistical Analysis
Descriptive Statistics: Mean, min, max, standard deviation
Temporal Aggregation: Daily and weekly grouping
Categorical Aggregation: Building-wise summaries
Peak Detection: Identify maximum consumption events
Key Insights
Based on typical campus energy data:

High Consumers: Science buildings use 2-3x more energy due to lab equipment
Weekly Patterns: Weekend usage drops 30-40% in most buildings
Peak Times: Highest consumption during weekday afternoons
Opportunities: Target top 2-3 buildings for 60-70% of potential savings
Recommendations for Energy Savings
Immediate Actions:
Install motion-sensor lighting in low-traffic areas
Schedule HVAC systems based on occupancy patterns
Educate staff on energy conservation
Short-term Improvements:
Upgrade to LED lighting campus-wide
Install programmable thermostats
Implement building automation systems
Long-term Investments:
Solar panel installation on high-consumption buildings
Energy-efficient HVAC replacement
Smart metering for real-time monitoring
Academic Integrity Statement
This project was completed individually as part of the Programming for Problem Solving course. All code is original work, with proper attribution for any external datasets or resources used.

Future Enhancements
Potential improvements for this project:

Interactive web dashboard using Plotly or Dash
Predictive modeling for future consumption
Real-time monitoring integration
Mobile app for facilities management
Integration with building automation systems
Author
[Your Name]
[Your Email]
Course: Programming for Problem Solving using Python

Acknowledgments
Dataset: Campus facilities department (or synthetic data for demonstration)
Course Instructor: jyoti.yadav@krmangalam.edu.in
Assignment: Capstone Project - Campus Energy-Use Dashboard
License
Educational project for course completion.

Last Updated: December 2025

