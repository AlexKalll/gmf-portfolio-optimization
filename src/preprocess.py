"""Data cleaning and preparation functions"""

import pandas as pd
import os

# Create processed data directory if it doesn't exist
os.makedirs('data/processed', exist_ok=True)

# Load the raw data
tsla = pd.read_csv('data/raw/TSLA.csv', index_col='Date', parse_dates=True)
bnd = pd.read_csv('data/raw/BND.csv', index_col='Date', parse_dates=True)
spy = pd.read_csv('data/raw/SPY.csv', index_col='Date', parse_dates=True)

# Select the 'Adj Close' column and rename it to the ticker
tsla_adj_close = tsla[['Adj Close']].rename(columns={'Adj Close': 'TSLA'})
bnd_adj_close = bnd[['Adj Close']].rename(columns={'Adj Close': 'BND'})
spy_adj_close = spy[['Adj Close']].rename(columns={'Adj Close': 'SPY'})

# Merge the data
merged_data = pd.concat([tsla_adj_close, bnd_adj_close, spy_adj_close], axis=1)

# Handle missing values
merged_data.fillna(method='ffill', inplace=True)

# Save the processed data
merged_data.to_csv('data/processed/merged_data.csv')

print("Data preprocessing complete.")