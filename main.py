from data_loader import load_data
from indicators import compute_rsi, compute_ema
from strategy import generate_signals
from backtest import backtest_strategy
from utils import plot_signals

def main():
    df = load_data('data/Binance_BTCUSDT_1h.csv')  # Replace with your data path
    df = compute_ema(df)
    df = compute_rsi(df)
    df = generate_signals(df)
    final_value = backtest_strategy(df)
    plot_signals(df)

if __name__ == '__main__':
    main()
