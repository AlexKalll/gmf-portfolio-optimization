"""Functions for MPT optimization and efficient frontier"""

import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns

# Load processed data
data = pd.read_csv('data/processed/merged_data.csv', index_col='Date', parse_dates=True)

# Calculate expected returns and sample covariance
mu = expected_returns.mean_historical_return(data)
S = risk_models.sample_cov(data)

# Optimize for maximal Sharpe ratio
ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()
cleaned_weights = ef.clean_weights()

print("Optimal Weights:")
print(cleaned_weights)
ef.portfolio_performance(verbose=True)

print("\nPortfolio optimization complete.")