def calculate_rsi(data, window=14):
    """
    Calculate the Relative Strength Index (RSI).
    """
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

def calculate_bollinger_bands(data, window=20):
    """
    Calculate Bollinger Bands.
    """
    data['BB_Middle'] = data['Close'].rolling(window=window).mean()
    data['BB_Upper'] = data['BB_Middle'] + 2 * data['Close'].rolling(window=window).std()
    data['BB_Lower'] = data['BB_Middle'] - 2 * data['Close'].rolling(window=window).std()
    return data
