import pandas as pd


def backtest_strategy(
    df: pd.DataFrame,
    initial_balance: float = 10000,
    transaction_fee: float = 0.00125,
    stop_loss: float = None,
    take_profit: float = None
) -> pd.Series:
    """
    Backtest a trading strategy.

    Args:
        df (pd.DataFrame): DataFrame with Close, Buy_Signal, Sell_Signal.
        initial_balance (float): Starting capital.
        transaction_fee (float): Fee per trade.
        stop_loss (float, optional): Stop-loss in decimal (e.g., 0.02 = 2%).
        take_profit (float, optional): Take-profit in decimal.

    Returns:
        pd.Series: Portfolio value over time.
    """
    balance = initial_balance
    position = 0.0
    portfolio_values = []

    for i in range(len(df)):
        price = df.iloc[i]['Close']

        # Buy
        if df.iloc[i]['Buy_Signal'] and position == 0:
            position = (balance * (1 - transaction_fee)) / price
            entry_price = price
            balance = 0.0

        # Sell
        elif df.iloc[i]['Sell_Signal'] and position > 0:
            balance = position * price * (1 - transaction_fee)
            position = 0.0

        # Stop-loss / Take-profit
        elif position > 0:
            if stop_loss and price <= entry_price * (1 - stop_loss):
                balance = position * price * (1 - transaction_fee)
                position = 0.0
            elif take_profit and price >= entry_price * (1 + take_profit):
                balance = position * price * (1 - transaction_fee)
                position = 0.0

        # Append portfolio value
        portfolio_values.append(balance + position * price)

    return pd.Series(portfolio_values, index=df.index)
