import pandas as pd
from src.liquidity_model import LiquidityModel
from src.visualization import plot_simulation


def main():
    deposits = pd.read_csv("data/deposits.csv")
    total_deposits = deposits["balance"].sum()

    model = LiquidityModel(
        total_deposits=total_deposits,
        buffer_ratio=0.20,
        days=1000
    )

    paths = [model.simulate_path() for _ in range(1000)]
    plot_simulation(paths, buffer_line=total_deposits * 0.20)


if __name__ == "__main__":
    main()