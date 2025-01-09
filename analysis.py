import pandas as pd

def calculate_returns(data):
    """
    Calculate daily and cumulative returns.
    """
    data['Daily Return'] = data['Close'].pct_change()
    data['Cumulative Return'] = (1 + data['Daily Return']).cumprod()
    return data

def calculate_moving_averages(data, windows=[20, 50]):
    """
    Calculate moving averages for specified window sizes.
    """
    for window in windows:
        data[f'{window}-Day MA'] = data['Close'].rolling(window=window).mean()
    return data

def calculate_volatility(data, window=20):
    """
    Calculate rolling volatility (standard deviation of daily returns).
    """
    data['Volatility'] = data['Daily Return'].rolling(window=window).std()
    return data

def compare_stock_returns(data_dict):
    """
    Compare daily returns of multiple stocks.
    :param data_dict: Dictionary with stock tickers as keys and DataFrames as values
    :return: DataFrame with daily returns for all stocks
    """
    returns = pd.DataFrame()
    for ticker, data in data_dict.items():
        returns[ticker] = data['Close'].pct_change()
    return returns

def calculate_correlation(returns):
    """
    Calculate correlation between stocks.
    :param returns: DataFrame of daily returns for all stocks
    :return: Correlation matrix
    """
    return returns.corr()