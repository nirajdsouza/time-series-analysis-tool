from data_fetch import fetch_stock_data
from analysis import calculate_returns, calculate_moving_averages, calculate_volatility, compare_stock_returns, calculate_correlation
from visualization import plot_closing_price, plot_moving_averages, plot_bollinger_bands, plot_correlation_heatmap, plot_rsi
from portfolio_analysis import efficient_frontier, plot_efficient_frontier
from forecasting import forecast_arima, plot_forecast
from config import TICKERS, PERIOD
from technical_indicators import calculate_rsi, calculate_bollinger_bands

import warnings
warnings.filterwarnings("ignore")

def main():
    # Step 1: Fetch data for multiple stocks
    data_dict = {ticker: fetch_stock_data(ticker, PERIOD) for ticker in TICKERS}


    # Step 2: Perform multi-stock analysis
    returns = compare_stock_returns(data_dict)
    correlation_matrix = calculate_correlation(returns)
    plot_correlation_heatmap(correlation_matrix, TICKERS)

    # Step 3: Efficient Frontier
    results, weights = efficient_frontier(returns)
    plot_efficient_frontier(results)

    # Step 4: Single Stock Analysis and Forecasting
    for ticker, data in data_dict.items():
        print(f"Analyzing {ticker}...")
        data = data.dropna()  # Drop rows with missing values
        data = calculate_returns(data)
        data = calculate_moving_averages(data)
        data = calculate_volatility(data)
        data = calculate_rsi(data)
        data = calculate_bollinger_bands(data)
        
        # Visualize individual stock data
        plot_closing_price(data, ticker)
        plot_moving_averages(data, ticker)
        plot_bollinger_bands(data, ticker)
        plot_rsi(data, ticker)

        
        # Forecast future stock price
        model_fit, forecast = forecast_arima(data)
        plot_forecast(data, forecast, steps=30)

if __name__ == "__main__":
    main()
