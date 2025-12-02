# Sample Data Generator
# Run this FIRST to create sample CSV files for testing

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

print("Generating sample energy data...")

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')
    print("✓ Created 'data' directory")

# Building names
buildings = ['Library', 'Science_Block', 'Admin_Building', 'Cafeteria', 'Sports_Complex']

# Generate data for each building
for building in buildings:
    print(f"Generating data for {building}...")
    
    # Create dates for last 90 days
    dates = []
    start_date = datetime.now() - timedelta(days=90)
    for i in range(90):
        current_date = start_date + timedelta(days=i)
        dates.append(current_date)
    
    # Generate realistic energy consumption data
    # Different buildings have different usage patterns
    if building == 'Library':
        base_usage = 150  # kWh per day
        variation = 30
    elif building == 'Science_Block':
        base_usage = 300  # High usage due to labs
        variation = 50
    elif building == 'Admin_Building':
        base_usage = 100
        variation = 20
    elif building == 'Cafeteria':
        base_usage = 200
        variation = 40
    else:  # Sports Complex
        base_usage = 180
        variation = 35
    
    # Generate random consumption values
    kwh_values = []
    for i in range(len(dates)):
        # Add some randomness and weekly patterns
        day_of_week = dates[i].weekday()
        
        # Lower usage on weekends (5=Saturday, 6=Sunday)
        if day_of_week >= 5:
            usage = base_usage * 0.6 + np.random.uniform(-variation/2, variation/2)
        else:
            usage = base_usage + np.random.uniform(-variation, variation)
        
        # Make sure usage is positive
        usage = max(usage, 10)
        kwh_values.append(round(usage, 2))
    
    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'kWh': kwh_values
    })
    
    # Save to CSV
    filename = f'data/{building}.csv'
    df.to_csv(filename, index=False)
    print(f"  ✓ Created {filename} with {len(df)} records")

print("\n✅ Sample data generation complete!")
print("You can now run the main energy dashboard script.")