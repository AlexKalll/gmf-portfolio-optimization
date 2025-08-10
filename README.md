# Time Series Forecasting for Portfolio Management Optimization

This project is focusing on applying time series forecasting to optimize portfolio management strategies for Guide Me in Finance (GMF) Investments.

## Business Objective

The primary goal is to leverage historical financial data to build predictive models that can forecast market trends, specifically for Tesla (TSLA), and use these insights to construct an optimized investment portfolio. The portfolio also includes a bond ETF (BND) for stability and an S&P 500 ETF (SPY) for broad market exposure.

## Project Tasks

1.  **Data Preprocessing and Exploration**: Fetched historical data for TSLA, BND, and SPY from Yahoo Finance, cleaned the data, and performed exploratory data analysis (EDA) to identify trends and patterns.
2.  **Time Series Forecasting**: Developed and compared ARIMA and LSTM models to forecast TSLA's stock price.
3.  **Portfolio Optimization**: Used the best-performing forecast model's output along with historical data for BND and SPY to construct an efficient frontier and identify optimal portfolios.
4.  **Strategy Backtesting**: Simulated the performance of the recommended portfolio against a benchmark to validate the strategy.

## Key Files and Directories

* `/data`: Contains raw and processed financial data.
* `/notebooks`: Jupyter notebooks for EDA, modeling, and backtesting.
* `/src`: Python scripts for data fetching, preprocessing, modeling, and portfolio optimization.
* `/docs`: The final investment memo.
* `requirements.txt`: A list of necessary Python libraries.

## How to Run

1.  Install the required libraries: `pip install -r requirements.txt`
2.  Run the Python scripts in the `/src` directory in the following order:
    * `data_fetch.py`
    * `preprocess.py`
    * `models.py`
    * `portfolio_optimization.py`
    * `backtesting.py`
3.  Explore the Jupyter notebooks in the `/notebooks` directory to see the analysis.