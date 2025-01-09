import matplotlib.pyplot as plt
import seaborn as sns

def plot_closing_price(data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Closing Price', color='blue', alpha=0.8)
    plt.title(f'{ticker} Closing Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

def plot_moving_averages(data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Closing Price', color='blue', alpha=0.5)
    for col in [col for col in data.columns if 'MA' in col]:
        plt.plot(data[col], label=col)
    plt.title(f'{ticker} Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

def plot_bollinger_bands(data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Closing Price', color='blue', alpha=0.5)
    plt.plot(data['BB_Upper'], label='Upper Band', color='green', linestyle='--')
    plt.plot(data['BB_Lower'], label='Lower Band', color='red', linestyle='--')
    plt.title(f'{ticker} Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()

def plot_correlation_heatmap(correlation_matrix, tickers):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', xticklabels=tickers, yticklabels=tickers)
    plt.title('Stock Correlation Heatmap')
    plt.show()
    
def plot_rsi(data, ticker):
    plt.figure(figsize=(12, 6))
    plt.plot(data['RSI'], label='RSI', color='purple', alpha=0.8)
    plt.title(f'{ticker} RSI Over Time')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()
