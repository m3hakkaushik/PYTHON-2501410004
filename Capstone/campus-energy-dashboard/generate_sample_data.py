# Sample Data Generator
# Run this FIRST to create sample CSV files for testing

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

print("Generating sample energy data...")


if not os.path.exists('data'):
    os.makedirs('data')
    print("✓ Created 'data' directory")


buildings = ['Library', 'Science_Block', 'Admin_Building', 'Cafeteria', 'Sports_Complex']


for building in buildings:
    print(f"Generating data for {building}...")
    
 
    dates = []
    start_date = datetime.now() - timedelta(days=90)
    for i in range(90):
        current_date = start_date + timedelta(days=i)
        dates.append(current_date)
  
    if building == 'Library':
        base_usage = 150 
        variation = 30
    elif building == 'Science_Block':
        base_usage = 300 
        variation = 50
    elif building == 'Admin_Building':
        base_usage = 100
        variation = 20
    elif building == 'Cafeteria':
        base_usage = 200
        variation = 40
    else: 
        base_usage = 180
        variation = 35
    

    kwh_values = []
    for i in range(len(dates)):
      
        day_of_week = dates[i].weekday()
        

        if day_of_week >= 5:
            usage = base_usage * 0.6 + np.random.uniform(-variation/2, variation/2)
        else:
            usage = base_usage + np.random.uniform(-variation, variation)
        

        usage = max(usage, 10)
        kwh_values.append(round(usage, 2))
    

    df = pd.DataFrame({
        'Date': dates,
        'kWh': kwh_values
    })
    
#saving
    filename = f'data/{building}.csv'
    df.to_csv(filename, index=False)
    print(f"  ✓ Created {filename} with {len(df)} records")

print("\n✅ Sample data generation complete!")
print("You can now run the main energy dashboard script.")
