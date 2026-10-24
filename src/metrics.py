import numpy as np

def cagr(returns, periods_per_year=252):
    """Compound annual growth rate of a daily return series, as a decimal (0.10 = 10%)."""
    returns = returns.dropna()
    years = returns.count() / periods_per_year
    final_equity = (1 + returns).prod()
    cagr_value = final_equity**(1/years) - 1
    return cagr_value


def ann_vol(returns, periods_per_year=252): 
    """Annualized volatility of a daily return series, as a decimal (0.17 = 17%)."""
    returns = returns.dropna()
    vol_daily = returns.std()
    vol_annual = vol_daily * np.sqrt(periods_per_year)
    return vol_annual


def sharpe(returns, periods_per_year=252): 
    """Annualized Sharpe ratio of a daily return series (unitless). Risk-free rate assumed zero."""
    returns = returns.dropna()
    sharpe_ratio = returns.mean() / returns.std() * np.sqrt(periods_per_year)
    return sharpe_ratio

def max_drawdown(returns):
    """Maximum drawdown as a negative decimal (−0.20 = a 20% fall from peak)"""
    returns = returns.dropna()
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_dd = drawdown.min()
    return max_dd
