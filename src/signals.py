def ma_signal(prices, window=50):
    """Return 1 when price is above its trailing window-day average, else 0"""
    ma = prices.rolling(window).mean()
    signal = (prices > ma).astype(int)
    return signal