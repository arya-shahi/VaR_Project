import yfinance as yf
import pandas as pd

# Step 1: Download data
data = yf.download("RELIANCE.NS", start="2022-01-01", end="2025-01-01")
data.to_csv("RELIANCE.csv")

# Step 2: Calculate daily returns
returns = data["Close"].pct_change().dropna()

returns.to_csv("daily_returns.csv")

print("Daily returns calculated and saved successfully")

# Step 3: Historical Value at Risk (VaR)

confidence_level = 0.95

var_95 = float(returns.quantile(1 - confidence_level))

print(f"95% Historical VaR: {var_95:.4f}")

import numpy as np

# Step 4: Monte Carlo VaR

num_simulations = 10000

mean_return = returns.mean()
std_return = returns.std()

simulated_returns = np.random.normal(
    mean_return,
    std_return,
    num_simulations
)

mc_var_95 = np.percentile(simulated_returns, 5)
print(f"95% Monte Carlo VaR: {mc_var_95:.4f}")


import matplotlib.pyplot as plt

plt.hist(returns, bins=50, alpha=0.7)
plt.axvline(var_95, color='red', linestyle='--', label='Historical VaR')
plt.axvline(mc_var_95, color='green', linestyle='--', label='Monte Carlo VaR')

plt.title("Return Distribution with VaR")
plt.legend()
plt.show()

