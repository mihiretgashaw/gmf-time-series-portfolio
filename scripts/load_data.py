import yfinance as yf
import pandas as pd

# List of tickers
tickers = ["TSLA", "BND", "SPY"]

# Download historical data

data = yf.download(tickers, start="2015-07-01", end="2025-07-31", group_by='ticker', auto_adjust=False)

# Process each ticker's data
all_dfs = []

for ticker in tickers:
    df = data[ticker].copy()
    # Calculate daily returns using Adj Close
    df['Daily Return'] = df['Adj Close'].pct_change()
    # Calculate 30-day rolling volatility of daily returns
    df['Volatility'] = df['Daily Return'].rolling(window=30).std()
    # Add a column with ticker name for identification
    df['Ticker'] = ticker
    # Reset index to have Date as a column
    df.reset_index(inplace=True)
    all_dfs.append(df)

# Concatenate all ticker data into one DataFrame
final_df = pd.concat(all_dfs, ignore_index=True)

# Save to CSV
final_df.to_csv("data/financial_data.csv", index=False)

print("Data saved to data/financial_data.csv")

