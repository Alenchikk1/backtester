import pandas as pd

def run_backtest(prices, signal):
    """Return a DataFrame with daily_return, position, strat_ret.
    Timing: signal at close t -> position held over day t+1."""
    if not prices.index.equals(signal.index):
        raise ValueError("prices and signal must have the same dates")
    daily_return = prices.pct_change()
    position = signal.shift(1)
    strat_ret = daily_return * position
    result = pd.DataFrame({"daily_return": daily_return,
                           "position": position,
                           "strat_ret": strat_ret})
    return result