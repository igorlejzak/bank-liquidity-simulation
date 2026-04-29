import numpy as np


class LiquidityModel:
    def __init__(self, total_deposits, buffer_ratio, days):
        self.total_deposits = total_deposits
        self.buffer = total_deposits * buffer_ratio
        self.days = days

    def simulate_path(self):
        cash = self.buffer
        path = [cash]

        for _ in range(self.days):
            withdrawal = np.random.uniform(0.001, 0.010) * self.total_deposits
            deposit = np.random.uniform(0.002, 0.012) * self.total_deposits
            cash = cash - withdrawal + deposit
            path.append(cash)

        return path