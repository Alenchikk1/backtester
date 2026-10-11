import sqlite3
import pandas as pd

def load_prices(db_path, ticker):
    """Return a DataFrame of adjusted closes for one ticker, indexed by date"""
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(
        "SELECT date, adj_close FROM prices WHERE ticker = ? ORDER BY date", conn, params=(ticker,),
        parse_dates=["date"], index_col="date"
    )
    conn.close()
    if df.empty:
        raise ValueError(f"No price data found for ticker {ticker}")
    return df