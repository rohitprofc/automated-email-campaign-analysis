import pandas as pd
import numpy as np
import datetime

# Generate sample data
np.random.seed(42)  # For reproducibility

# Generate a date range
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Create sample data
data = {
    'date': np.random.choice(date_range, size=1000),
    'segment': np.random.choice(['Segment A', 'Segment B', 'Segment C'], size=1000),
    'opened': np.random.choice([0, 1], size=1000, p=[0.3, 0.7]),  # 70% opened rate
    'clicked': np.random.choice([0, 1], size=1000, p=[0.7, 0.3])  # 30% clicked rate
}

# Create DataFrame
df = pd.DataFrame(data)

# Sort by date for better representation
df = df.sort_values('date').reset_index(drop=True)

# Save to CSV
df.to_csv('email_campaign_data.csv', index=False)

print("Sample email_campaign_data.csv file generated.")
