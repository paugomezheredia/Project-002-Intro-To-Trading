import optuna
from indicators import compute_rsi, compute_ema
from signals import generate_signals
from backtest import backtest_strategy
from metrics import compute_metrics
import pandas as pd


def objective(trial, df: pd.DataFrame):
    """
    Objective function for Optuna optimization.

    Hyperparameters to tune:
        - RSI period
        - EMA span
        - RSI thresholds
        - Stop-loss and take-profit
    """
    # Sample hyperparameters
    rsi_period = trial.suggest_int("rsi_period", 7, 21)
    ema_span = trial.suggest_int("ema_span", 10, 50)
    rsi_buy = trial.suggest_int("rsi_buy", 20, 40)
    rsi_sell = trial.suggest_int("rsi_sell", 60, 80)
    stop_loss = trial.suggest_float("stop_loss", 0.01, 0.05)
    take_profit = trial.suggest_float("take_profit", 0.01, 0.1)

    # Compute indicators
    df_opt = df.copy()
    df_opt = compute_rsi(df_opt, period=rsi_period)
    df_opt = compute_ema(df_opt, span=ema_span)

    # Generate signals
    df_opt = generate_signals(df_opt, ema_column=f'EMA_{ema_span}',
                              rsi_buy=rsi_buy, rsi_sell=rsi_sell)

    # Backtest
    portfolio_values = backtest_strategy(df_opt, stop_loss=stop_loss, take_profit=take_profit)

    # Compute metrics
    metrics = compute_metrics(portfolio_values)

    # Use Calmar ratio as objective
    return metrics["Calmar"]


def optimize_strategy(df: pd.DataFrame, n_trials: int = 50):
    """
    Run Optuna optimization to find best hyperparameters.

    Returns:
        optuna.study.Study: Study object with optimization results.
    """
    study = optuna.create_study(direction="maximize")
    study.optimize(lambda trial: objective(trial, df), n_trials=n_trials)
    return study
