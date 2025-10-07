import pandas as pd


def generate_signals(df: pd.DataFrame, ema_column: str = 'EMA_20',
                     rsi_buy: int = 30, rsi_sell: int = 70) -> pd.DataFrame:
    """
    Generate buy/sell signals based on RSI and EMA crossover.

    Args:
        df (pd.DataFrame): DataFrame with price, RSI, and EMA columns.
        ema_column (str): EMA column name.
        rsi_buy (int): RSI threshold for buy.
        rsi_sell (int): RSI threshold for sell.

    Returns:
        pd.DataFrame: Original DataFrame with 'Buy_Signal' and 'Sell_Signal'.
    """
    if 'RSI' not in df.columns:
        raise KeyError("DataFrame must contain 'RSI' column.")
    if ema_column not in df.columns:
        raise KeyError(f"DataFrame must contain '{ema_column}' column.")

    df['Buy_Signal'] = (df['RSI'] < rsi_buy) & (df['Close'] > df[ema_column])
    df['Sell_Signal'] = (df['RSI'] > rsi_sell) & (df['Close'] < df[ema_column])

    return df
