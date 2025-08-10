"""Functions to fetch financial data using YFinance"""

import yfinance as yf
import pandas as pd
import os

# Create data directories if they don't exist
os.makedirs('data/raw', exist_ok=True)

# Define the tickers and the date range
tickers = ['TSLA', 'BND', 'SPY']
start_date = '2015-07-01'
end_date = '2025-07-31'

# Fetch the data
for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)
    data.to_csv(f'data/raw/{ticker}.csv')

print("Data fetching complete.")