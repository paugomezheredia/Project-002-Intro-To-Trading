import pandas as pd


def compute_rsi(df: pd.DataFrame, column: str = 'Close', period: int = 14) -> pd.DataFrame:
    """
    Calculate the Relative Strength Index (RSI).

    Args:
        df (pd.DataFrame): DataFrame with price data.
        column (str): Column to calculate RSI on. Default is 'Close'.
        period (int): Lookback period. Default is 14.

    Returns:
        pd.DataFrame: Original DataFrame with 'RSI' column added.
    """
    delta = df[column].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df


def compute_ema(df: pd.DataFrame, column: str = 'Close', span: int = 20) -> pd.DataFrame:
    """
    Calculate Exponential Moving Average (EMA).

    Args:
        df (pd.DataFrame): DataFrame with price data.
        column (str): Column to calculate EMA on. Default is 'Close'.
        span (int): Span for EMA. Default is 20.

    Returns:
        pd.DataFrame: Original DataFrame with EMA column added.
    """
    df[f'EMA_{span}'] = df[column].ewm(span=span, adjust=False).mean()
    return df
