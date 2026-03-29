import pandas as pd
import numpy as np

# Read CSV with empty strings as NaN
df = pd.read_csv('data/sample_data.csv', keep_default_na=False, na_values=[''])

print("ORIGINAL DATA:")
print(df)
print("\nMissing values before:")
print(df.isnull().sum())

# Fill numeric columns with mean
df['experiment_score'] = df['experiment_score'].fillna(df['experiment_score'].mean())
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
df['humidity'] = df['humidity'].fillna(df['humidity'].mean())

# Save
df.to_csv('data/cleaned_data.csv', index=False)

print("\n\nCLEANED DATA:")
print(df)
print("\nMissing values after:")
print(df.isnull().sum())
print("\n✓ Cleaned data saved to 'data/cleaned_data.csv'")