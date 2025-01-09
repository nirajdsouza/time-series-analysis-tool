from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def forecast_arima(data, column='Close', order=(5, 1, 0), steps=30):
    """
    Fit ARIMA model and forecast future values.
    """
    model = ARIMA(data[column], order=order)
    model_fit = model.fit()

    # Forecast future values
    forecast = model_fit.forecast(steps=steps)
    return model_fit, forecast

def plot_forecast(data, forecast, steps, column='Close'):
    """
    Plot the forecasted values along with historical data.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data[column], label='Historical', color='blue')
    plt.plot(range(len(data), len(data) + steps), forecast, label='Forecast', color='orange')
    plt.title('ARIMA Stock Price Forecast')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
