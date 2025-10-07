import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from metrics import compute_metrics


def generate_performance_report(portfolio_values: pd.Series, title: str = "Strategy Performance"):
    """
    Generate performance metrics, plots, and returns tables.

    Args:
        portfolio_values (pd.Series): Portfolio value over time.
        title (str): Plot title.
    """
    # 1. Compute performance metrics
    metrics = compute_metrics(portfolio_values)
    print("Performance Metrics:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}" if value is not None else f"{key}: N/A")
    print("\n")

    # 2. Portfolio value chart
    plt.figure(figsize=(12, 6))
    plt.plot(portfolio_values, label='Portfolio Value', color='blue')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.show()

    # 3. Monthly, Quarterly, Annual Returns
    returns = portfolio_values.pct_change().dropna()
    monthly = returns.resample('M').apply(lambda x: (1 + x).prod() - 1)
    quarterly = returns.resample('Q').apply(lambda x: (1 + x).prod() - 1)
    annually = returns.resample('A').apply(lambda x: (1 + x).prod() - 1)

    returns_tables = {
        "Monthly Returns": monthly,
        "Quarterly Returns": quarterly,
        "Annual Returns": annually
    }

    for name, table in returns_tables.items():
        print(f"{name}:")
        print(table.to_frame(name='Return'))
        print("\n")

    # 4. Returns distribution using Seaborn
    plt.figure(figsize=(10, 5))
    sns.histplot(returns, bins=50, kde=True, color='skyblue')
    plt.title("Distribution of Daily Returns")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.show()
