import pandas as pd
from pathlib import Path


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load trading data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the trading data.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    df = pd.read_csv(file_path)
    print(f"Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


if __name__ == "__main__":
    # Example usage
    data = load_data("trading_data.csv")

