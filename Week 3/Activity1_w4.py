"""
Activity 1: read and extract the csv file
"""
import pandas as pd

# Correct way to define the file path
file_path = 'Week 3/sample_junk_mail.csv'  # Use forward slashes or raw string

# Load CSV
df = pd.read_csv(file_path)

# Print first 5 rows
print(df.head())

# Access specific column
print(df['EmailID'])

# Iterate over rows
for index, row in df.iterrows():
    print(row['IsSpam'], row['Subject'] ,row['EmailID'])
    # Example: print(row['Subject'], row['Body']) if these exist
