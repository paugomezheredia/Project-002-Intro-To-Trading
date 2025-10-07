import pandas as pd


def generate_signals(df: pd.DataFrame, ema_column: str = 'EMA_20') -> pd.DataFrame:
    """
    Generate buy and sell signals based on RSI and EMA crossover.

    Buy Signal:
        - RSI is below 30 (oversold condition)
        - Close price is above the EMA

    Sell Signal:
        - RSI is above 70 (overbought condition)
        - Close price is below the EMA

    Args:
        df (pd.DataFrame): DataFrame containing trading data with 'RSI' and EMA columns.
        ema_column (str, optional): Name of the EMA column to use. Defaults to 'EMA_20'.

    Returns:
        pd.DataFrame: Original DataFrame with 'Buy_Signal' and 'Sell_Signal' columns added.
    """
    if 'RSI' not in df.columns:
        raise KeyError("The DataFrame must contain an 'RSI' column.")
    if ema_column not in df.columns:
        raise KeyError(f"The DataFrame must contain the '{ema_column}' column.")

    df['Buy_Signal'] = (df['RSI'] < 30) & (df['Close'] > df[ema_column])
    df['Sell_Signal'] = (df['RSI'] > 70) & (df['Close'] < df[ema_column])

    return df

