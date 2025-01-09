
# Stock Analysis and Forecasting Tool

This project is a learning tool developed to analyze and forecast stock data using Python. It fetches historical stock data, performs technical analysis, visualizes key metrics, and forecasts future stock prices using the ARIMA model.

## Features

-   **Fetch Stock Data**: Download historical stock data from Yahoo Finance.
-   **Technical Analysis**:
    -   Calculate daily returns, moving averages, volatility, and RSI (Relative Strength Index).
    -   Calculate Bollinger Bands for stock price volatility analysis.
-   **Forecasting**: Use ARIMA to forecast future stock prices.
-   **Efficient Frontier**: Analyze portfolio optimization and visualize the efficient frontier.
-   **Visualization**:
    -   Visualize stock prices, moving averages, Bollinger Bands, and correlation heatmaps.

## Requirements

-   Python 3.x
-   `pandas`
-   `numpy`
-   `matplotlib`
-   `seaborn`
-   `yfinance`
-   `statsmodels`

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Configuration

In the `config.py` file, you can configure the stock tickers (`TICKERS`) and the period (`PERIOD`) for which the data will be fetched (e.g., '5y' for 5 years of data).

## Usage
1.  Run the `main.py` script:
    
    ```bash
    python main.py
    ```
    

This will:

-   Fetch data for the configured stock tickers.
-   Perform analysis, including returns, moving averages, volatility, and RSI.
-   Forecast future stock prices.
-   Visualize the data and metrics for each stock.

## License

[MIT](LICENSE) License.