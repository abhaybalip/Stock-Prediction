import os
import yfinance as yf
import pandas as pd

def get_historical(quote):
    try:
        # Download 2 years of historical data with daily interval
        data = yf.download(quote, period="2y", interval="1d")
        if data.empty:
            raise ValueError(f"No data found for stock symbol: {quote}")

        # Reset index to have 'Date' as a column
        data.reset_index(inplace=True)
        data['Code'] = quote  # Add stock symbol column

        # Create 'data' folder if not exists
        os.makedirs('data', exist_ok=True)
        data.to_csv(f'data/{quote}.csv', index=False)

        return data
    except Exception as e:
        raise ValueError(f"Error downloading data: {str(e)}")
