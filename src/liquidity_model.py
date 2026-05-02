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
            stress = np.random.random() < 0.05  # 5% szans na stresowy dzień

            if stress:
                withdrawal = np.random.uniform(0.010, 0.020) * self.total_deposits
                deposit = np.random.uniform(0.003, 0.006) * self.total_deposits
            else:
                withdrawal = np.random.uniform(0.003, 0.008) * self.total_deposits
                deposit = np.random.uniform(0.003, 0.009) * self.total_deposits

            cash = cash - withdrawal + deposit
            path.append(cash)

        return path