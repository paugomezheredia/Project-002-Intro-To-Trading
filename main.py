import pandas as pd
from indicators import compute_rsi, compute_ema
from signals import generate_signals
from backtest import backtest_strategy
from reporting import generate_performance_report

# Load data
df = pd.read_csv("data/Binance_BTCUSDT_1h.csv", parse_dates=['Date'], index_col='Date')

# Compute indicators
df = compute_rsi(df, period=14)
df = compute_ema(df, span=20)

# Generate signals
df = generate_signals(df, ema_column='EMA_20')

# Backtest strategy
portfolio_values = backtest_strategy(df, initial_balance=10000, transaction_fee=0.00125)

# Generate performance report
generate_performance_report(portfolio_values)
