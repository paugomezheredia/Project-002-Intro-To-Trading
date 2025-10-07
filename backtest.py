import pandas as pd


def backtest_strategy(
    df: pd.DataFrame,
    initial_balance: float = 10000,
    transaction_fee: float = 0.00125  # 0.125% per trade
) -> float:
    """
    Run a simple backtest using generated buy/sell signals.

    Args:
        df (pd.DataFrame): DataFrame containing 'Close', 'Buy_Signal', and 'Sell_Signal' columns.
        initial_balance (float, optional): Starting capital. Defaults to 10,000.
        transaction_fee (float, optional): Proportional transaction fee per trade (e.g., 0.00125 = 0.125%). Defaults to 0.00125.

    Returns:
        float: Final portfolio value.
    """
    balance = initial_balance
    position = 0.0

    for i in range(len(df)):
        close_price = df.loc[i, 'Close']

        # Buy signal: enter long if no position
        if df.loc[i, 'Buy_Signal'] and position == 0:
            position = (balance * (1 - transaction_fee)) / close_price
            balance = 0.0

        # Sell signal: exit position
        elif df.loc[i, 'Sell_Signal'] and position > 0:
            balance = position * close_price * (1 - transaction_fee)
            position = 0.0

    # Final portfolio value
    final_value = balance + (position * df.iloc[-1]['Close'])
    print(f"Final portfolio value: ${final_value:,.2f}")

    return final_value

