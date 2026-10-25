def ma_signal(prices, window=50):
    """Return 1 when price is above its trailing window-day average, else 0"""
    ma = prices.rolling(window).mean()
    signal = (prices > ma).astype(int)
    return signal

def momentum_signal(prices, lookback=252):
    """Return 1 when price is above its level lookback days ago (positive trailing return), else 0"""
    lookback_prices = prices.shift(lookback)
    trailing_return = prices / lookback_prices - 1
    signal = (trailing_return > 0).astype(int)
    return signal


