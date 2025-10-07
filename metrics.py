import pandas as pd
import numpy as np


def compute_metrics(portfolio_values: pd.Series, risk_free_rate: float = 0.0) -> dict:
    """
    Compute strategy performance metrics.

    Args:
        portfolio_values (pd.Series): Portfolio value over time.
        risk_free_rate (float): Daily risk-free rate (default 0).

    Returns:
        dict: Calmar, Sharpe, Sortino, MDD, and Win Rate.
    """
    returns = portfolio_values.pct_change().dropna()
    total_return = (portfolio_values.iloc[-1] / portfolio_values.iloc[0]) - 1
    annualized_return = (1 + total_return) ** (252 / len(returns)) - 1

    # Maximum Drawdown
    cum_max = portfolio_values.cummax()
    drawdown = (portfolio_values - cum_max) / cum_max
    max_drawdown = drawdown.min()

    # Sharpe Ratio
    sharpe = (returns.mean() - risk_free_rate / 252) / returns.std() * np.sqrt(252)

    # Sortino Ratio
    downside = returns[returns < 0]
    sortino = (returns.mean() - risk_free_rate / 252) / downside.std() * np.sqrt(252) if not downside.empty else np.nan

    # Calmar Ratio
    calmar = annualized_return / abs(max_drawdown) if max_drawdown != 0 else np.nan

    # Win Rate
    trades = returns[returns != 0]
    win_rate = (trades > 0).sum() / len(trades) if len(trades) > 0 else np.nan

    return {
        "Calmar": calmar,
        "Sharpe": sharpe,
        "Sortino": sortino,
        "Max_Drawdown": max_drawdown,
        "Win_Rate": win_rate
    }
