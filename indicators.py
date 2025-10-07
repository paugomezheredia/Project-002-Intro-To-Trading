import pandas as pd


def compute_rsi(df: pd.DataFrame, column: str = 'Close', period: int = 14) -> pd.DataFrame:
    """
    Calculate the Relative Strength Index (RSI) for a given column in a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing trading data.
        column (str, optional): Column name to calculate RSI on. Defaults to 'Close'.
        period (int, optional): Lookback period for RSI calculation. Defaults to 14.

    Returns:
        pd.DataFrame: Original DataFrame with an additional 'RSI' column.
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
    Calculate the Exponential Moving Average (EMA) for a given column in a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing trading data.
        column (str, optional): Column name to calculate EMA on. Defaults to 'Close'.
        span (int, optional): Span for the EMA calculation. Defaults to 20.

    Returns:
        pd.DataFrame: Original DataFrame with an additional EMA column.
    """
    df[f'EMA_{span}'] = df[column].ewm(span=span, adjust=False).mean()
    return df

