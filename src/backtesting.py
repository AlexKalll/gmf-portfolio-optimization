"""Simulation and performance analysis functions"""

import pandas as pd

# Load processed data
data = pd.read_csv('data/processed/merged_data.csv', index_col='Date', parse_dates=True)
returns = data.pct_change().dropna()

# Define backtesting period (last year of data)
backtest_start_date = '2024-08-01'
backtest_returns = returns[backtest_start_date:]

# Optimal weights from portfolio_optimization.py (example weights)
optimal_weights = {'TSLA': 0.3, 'BND': 0.4, 'SPY': 0.3} # Replace with actual optimized weights

# Benchmark weights
benchmark_weights = {'SPY': 0.6, 'BND': 0.4, 'TSLA': 0.0}

# Calculate portfolio returns
backtest_returns['optimized_portfolio'] = (backtest_returns * pd.Series(optimal_weights)).sum(axis=1)
backtest_returns['benchmark_portfolio'] = (backtest_returns * pd.Series(benchmark_weights)).sum(axis=1)

# Calculate cumulative returns
cumulative_returns = (1 + backtest_returns[['optimized_portfolio', 'benchmark_portfolio']]).cumprod() - 1

# Plot cumulative returns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
cumulative_returns['optimized_portfolio'].plot(label='Optimized Portfolio')
cumulative_returns['benchmark_portfolio'].plot(label='Benchmark Portfolio')
plt.title('Backtesting Results: Optimized vs. Benchmark Portfolio')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.savefig('images/backtest_results.png')
plt.show()

print("Backtesting complete. Plot saved to images/backtest_results.png")