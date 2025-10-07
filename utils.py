import matplotlib.pyplot as plt
import pandas as pd


def plot_signals(df: pd.DataFrame, portfolio_values: pd.Series = None, ema_column: str = 'EMA_20') -> None:
    """
    Visualize trading signals and related indicators.

    Args:
        df (pd.DataFrame): DataFrame containing 'Close', 'Buy_Signal', 'Sell_Signal', 'RSI', and EMA columns.
        portfolio_values (pd.Series, optional): Series of portfolio value over time. Defaults to None.
        ema_column (str, optional): Name of the EMA column. Defaults to 'EMA_20'.
    """
    # 1. Close price with buy/sell signals
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', alpha=0.5)
    plt.scatter(df.index[df['Buy_Signal']], df['Close'][df['Buy_Signal']], label='Buy', marker='^', color='green')
    plt.scatter(df.index[df['Sell_Signal']], df['Close'][df['Sell_Signal']], label='Sell', marker='v', color='red')
    plt.title('Trading Signals')
    plt.legend()
    plt.show()

    # 2. RSI over time
    if 'RSI' in df.columns:
        plt.figure(figsize=(12, 4))
        plt.plot(df['RSI'], label='RSI', color='purple')
        plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
        plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
        plt.title('RSI Indicator')
        plt.legend()
        plt.show()

    # 3. EMA vs. Close price
    if ema_column in df.columns:
        plt.figure(figsize=(12, 6))
        plt.plot(df['Close'], label='Close Price', alpha=0.5)
        plt.plot(df[ema_column], label=ema_column, color='orange')
        plt.title('Close Price vs EMA')
        plt.legend()
        plt.show()

    # 4. Portfolio value over time (if provided)
    if portfolio_values is not None:
        plt.figure(figsize=(12, 6))
        plt.plot(portfolio_values, label='Portfolio Value', color='blue')
        plt.title('Portfolio Value Over Time')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.show()


import seaborn as sns


def plot_returns_distribution(df: pd.DataFrame, column: str = 'Close') -> None:
    """
    Plot the distribution of daily returns using Seaborn.

    Args:
        df (pd.DataFrame): DataFrame containing a price column.
        column (str, optional): Name of the column to calculate returns. Defaults to 'Close'.
    """
    if column not in df.columns:
        raise KeyError(f"The DataFrame must contain the '{column}' column.")

    # Calculate daily returns
    df['Returns'] = df[column].pct_change()

    # Plot distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Returns'].dropna(), bins=50, kde=True, color='skyblue')
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.show()

