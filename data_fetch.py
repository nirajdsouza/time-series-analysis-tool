import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, period="5y"):
    """
    Fetch historical stock data for the given ticker.
    :param ticker: Stock ticker symbol (e.g., 'AAPL')
    :param period: Time period (e.g., '5y' for 5 years)
    :return: DataFrame with stock data
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data
