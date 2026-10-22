import pandas as pd

def run_backtest(prices, signal, cost_bps=0):
    """Return a DataFrame with daily_return, position, strat_ret, turnover and net_ret.
    Costs: cost_bps charged per unit of turnover, on the day the position changes
    Timing: signal at close t -> position held over day t+1."""
    if not prices.index.equals(signal.index):
        raise ValueError("prices and signal must have the same dates")
    daily_return = prices.pct_change()
    position = signal.shift(1).fillna(0)
    strat_ret = daily_return * position
    cost = cost_bps / 10_000
    turnover = position.diff().fillna(0).abs()
    net_ret = strat_ret - turnover * cost
    result = pd.DataFrame({"daily_return": daily_return,
                           "position": position,
                           "strat_ret": strat_ret,
                           "turnover": turnover,
                           "net_ret": net_ret})
    return result