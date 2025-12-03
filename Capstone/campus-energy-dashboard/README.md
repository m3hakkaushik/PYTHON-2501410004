# Campus Energy-Use Dashboard

## Project Overview

This capstone project analyzes electricity consumption data from multiple campus buildings to identify energy-saving opportunities. The system automatically reads meter data, performs statistical analysis, and generates visual dashboards to support administrative decision-making.

## Terminal + outcome

<img width="1132" height="231" alt="Screenshot 2025-12-02 at 4 20 13 PM" src="https://github.com/user-attachments/assets/d50eda54-5a35-4fee-94a6-5e77faecc25a" />
<img width="1448" height="477" alt="Screenshot 2025-12-02 at 4 20 39 PM" src="https://github.com/user-attachments/assets/458cba69-7fc3-4fad-a6a0-6e6d93d0bda8" />
<img width="1438" height="584" alt="Screenshot 2025-12-02 at 4 20 51 PM" src="https://github.com/user-attachments/assets/9604abf8-8926-4455-a50f-3796e712a39a" />
<img width="1025" height="295" alt="Screenshot 2025-12-02 at 4 21 46 PM" src="https://github.com/user-attachments/assets/36b091db-5362-4236-b157-76ba83dd978f" />


## Real-World Application

The campus facilities team can use this dashboard to:
  1. Identify high-consumption buildings for targeted energy-saving initiatives
  2. Monitor daily and weekly usage patterns
  3. Detect unusual spikes in energy consumption
  4. Plan renewable energy installations based on usage data
  5. Make informed decisions about building operations
      
## Dataset Description

The project processes multiple CSV files, each representing a building's monthly meter readings:

**Required CSV Format:**
  1. `Date` : Date of meter reading (YYYY-MM-DD format)
  2. `kWh` : Energy consumption in kilowatt-hours
     
**Sample Buildings:**
  1. Library
  2. Science Block
  3. Admin Building
  4. Cafeteria
  5. Sports Complex
     
Each CSV file should be named after the building (e.g., `Library.csv` , `Science_Block.csv` )

## Tools and Libraries Used
  1. **Python 3.x:** Core programming language
  2. **Pandas:** Data loading, cleaning, and aggregation
  3. **Matplotlib:** Creating visualizations and charts
  4. **NumPy:** Numerical calculations
  5. **os/pathlib:** File system operations
  6. **datetime:** Date and time handling

## Installation Instructions
  1. **Prerequisites :**
       
  Make sure you have Python 3.x installed on your computer.
    
  2. **Install Required Libraries:**
    
    pip install pandas matplotlib numpy
    
  3. **Project Setup:**
    

    #Clone the repository:     
      git clone https://github.com/m3hakkaushik/PYTHON-2501410004/tree/3f88dccec4aedaa2d4de82eba7ed0959af1c2c0e/Capstone/campus-energy-dashboard
     
    #Project structure will be created automatically``

  
## How to Use

**Step 1: Generate Sample Data (For Testing)**
If you don't have real data yet, run the sample data generator:


    python generate_sample_data.py
    
This creates a ``data/`` folder with sample CSV files for 5 buildings.

**Step 2: Run the Main Analysis**

    python energy_dashboard.py
    
**Step 3: Check the Output**

The program will create:

  1. ``output/cleaned_energy_data.csv`` - All building data combined and cleaned
  2. ``output/building_summary.csv`` - Statistical summary for each building
  3. ``output/summary.txt`` - Executive summary report
  4.``dashboard.png`` - Visual dashboard with 3 charts

## Project Architecture

***Object-Oriented Design***

**1. MeterReading Class**

Represents a single electricity meter reading.

  1. Stores timestamp and kWh value
  2. Provides string representation for debugging
     
**2. Building Class**

Represents a campus building with all its meter readings.

**Attributes:**

1. `name:` Building name
2. `meter_readings:` List of MeterReading objects
   
**Methods:**

  1. ``add_reading()``: Add a new meter reading
  2. ``calculate_total_consumption()``: Sum all readings
  3. ``calculate_average_consumption()``: Calculate mean usage
  4. ``calculate_min_consumption()``: Find minimum reading
  5. ``calculate_max_consumption()``: Find maximum reading
  6. ``generate_report()``: Create text summary
     
**3. BuildingManager Class**

Manages all buildings on campus.

**Attributes:**

``buildings``: Dictionary of Building objects

**Methods:**

  1. ``add_building()``: Register a new building
  2. ``get_building()``: Retrieve building by name
  3. ``get_all_buildings()``: List all building names
  4. ``get_total_campus_consumption()``: Calculate campus-wide total
  5. ``get_highest_consuming_building()``: Identify top consumer
     
**Core Functions**

*Data Aggregation Functions*
``calculate_daily_totals(df)``

  1. Groups data by date
  2. Sums kWh for each day
  3. Returns DataFrame with daily totals
     
``calculate_weekly_aggregates(df)``

  1. Uses Pandas resample to group by week
  2. Calculates weekly consumption totals
  3. Useful for identifying weekly patterns

``building_wise_summary(df)``

  1. Creates dictionary with statistics per building
  2. Calculates mean, min, max, and total for each building
  3. Returns structured summary data

## Features Implemented

**Task 1: Data Ingestion and Validation ✓**

  1. Automatically scans data/ directory for CSV files
  2. Handles missing files with try-except blocks
  3. Skips corrupt data lines
  4. Logs loading status for each file
  5. Combines all files into single DataFrame

**Task 2: Core Aggregation Logic ✓**

1.   Daily consumption totals
2.   Weekly aggregated statistics
3.   Building-wise summaries with mean, min, max, total
4.   Uses groupby and resample operations

**Task 3: Object-Oriented Modeling ✓**

1.   MeterReading class for individual readings
2.   Building class with consumption methods
3.   BuildingManager class for campus-wide operations
4.   Clear separation of concerns

**Task 4: Visual Output with Matplotlib ✓**

Creates dashboard with 3 visualizations:

1.   ``Trend Line Chart``: Daily consumption over time for all buildings
2.   ``Bar Chart``: Average weekly usage comparison across buildings
3.   ``Scatter Plot``: Consumption patterns by building and time
   All charts combined in single PNG with proper labels and legends.

**Task 5: Persistence and Executive Summary ✓**

Exports:

-   Cleaned dataset (CSV)
-   Building summary statistics (CSV)
-   Executive summary report (TXT)
  
Report includes:

- Total campus consumption
- Highest-consuming building
- Peak load time and location
- Daily and weekly trends
- Building-by-building breakdown
- Recommendations for energy saving
  
**Output Examples**

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
          
**Dashboard Visualization**
The ``dashboard.png`` contains:

- Top: Line chart showing daily trends
- Middle: Bar chart comparing buildings
- Bottom: Scatter plot of consumption patterns
  
**Executive Summary (summary.txt)**

    TOTAL CAMPUS CONSUMPTION: 67,845.23 kWh

    HIGHEST CONSUMING BUILDING:
      Science_Block: 24,532.10 kWh

    RECOMMENDATIONS:
    - Focus energy-saving initiatives on high-consumption buildings
    - Monitor peak usage times for load management
    
**Error Handling**

The program includes robust error handling:

- **FileNotFoundError:** Gracefully handles missing CSV files
- **Corrupt Data:** Skips bad lines using on_bad_lines='skip'
- **Missing Columns:** Validates required columns exist
- **Empty Data:** Checks for empty DataFrames before processing
- **Date Parsing:** Uses errors='coerce' for invalid dates
  
## File Structure

<img width="669" height="448" alt="Screenshot 2025-12-03 at 2 46 34 PM" src="https://github.com/user-attachments/assets/9e78d301-3ea2-45c5-845f-c9747874985f" />

## Methodology

_Data Processing Pipeline_

1. Ingestion: Load all CSV files from data directory
2. Validation: Check for required columns and valid data
3. Cleaning: Remove missing values, convert dates
4. Object Creation: Build Building objects with readings
5. Aggregation: Calculate daily, weekly, and building stats
6. Visualization: Create multi-chart dashboard
7. Export: Save cleaned data, summaries, and reports
   
_Statistical Analysis_

1. Descriptive Statistics: Mean, min, max, standard deviation
2. Temporal Aggregation: Daily and weekly grouping
3. Categorical Aggregation: Building-wise summaries
4. Peak Detection: Identify maximum consumption events
   
## Key Insights

Based on typical campus energy data:

- High Consumers: Science buildings use 2-3x more energy due to lab equipment
- Weekly Patterns: Weekend usage drops 30-40% in most buildings
- Peak Times: Highest consumption during weekday afternoons
- Opportunities: Target top 2-3 buildings for 60-70% of potential savings

## Recommendations for Energy Savings

1. Immediate Actions:

- Install motion-sensor lighting in low-traffic areas
- Schedule HVAC systems based on occupancy patterns
- Educate staff on energy conservation

2. Short-term Improvements:

- Upgrade to LED lighting campus-wide
- Install programmable thermostats
- Implement building automation systems

3. Long-term Investments:

- Solar panel installation on high-consumption buildings
- Energy-efficient HVAC replacement
- Smart metering for real-time monitoring
  
## Academic Integrity Statement

This project was completed individually as part of the Programming for Problem Solving course. All code is original work, with proper attribution for any external datasets or resources used.

## Future Enhancements

Potential improvements for this project:

- Interactive web dashboard using Plotly or Dash
- Predictive modeling for future consumption
- Real-time monitoring integration
- Mobile app for facilities management
- Integration with building automation systems
  
## Author
Mehak
Course: Programming for Problem Solving using Python

## Acknowledgments

- Dataset: Campus facilities department (or synthetic data for demonstration)
- Course Instructor: jyoti.yadav@krmangalam.edu.in
- Assignment: Capstone Project - Campus Energy-Use Dashboard

## License
Educational project for course completion.

----

**Last Updated:** December 2025

**
