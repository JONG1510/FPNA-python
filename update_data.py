import yfinance as yf
import pandas as pd
from datetime import datetime

def update_silver():
    # Define tickers: Silver (SI=F)
    tickers = ["SI=F"]
    
    # Fetch last 30 days of data
    # data = yf.download(tickers, period="1mo", interval="1d")['Close'] -- Only fetch Close prices
    data = yf.download(tickers, period="1mo", interval="1d")
    
    # Clean and save
    data.to_csv('data/SI_latest.csv')
    print(f"Data updated successfully at {datetime.now()}")

if __name__ == "__main__":
    update_silver()
  
