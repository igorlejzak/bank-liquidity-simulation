import numpy as np
import matplotlib.pyplot as plt


def plot_simulation(paths, buffer_line):
    paths = np.array(paths)
    final_values = paths[:, -1]

    worst = np.argmin(final_values)
    best = np.argmax(final_values)

    plt.figure(figsize=(12, 6))

    for path in paths:
        plt.plot(path, color="gray", alpha=0.15)

    plt.plot(paths[worst], color="red", linewidth=2, label="Worst scenario")
    plt.plot(paths[best], color="green", linewidth=2, label="Best scenario")
    plt.axhline(y=buffer_line, color="blue", linestyle="--", label="Minimum buffer (20%)")

    plt.xlabel("Day")
    plt.ylabel("Liquidity buffer")
    plt.title("Bank Liquidity Simulation - 1000 days")
    plt.legend()
    plt.tight_layout()
    plt.show()