
#  Value at Risk (VaR) Analysis using Python

*A practical risk-management project using real stock market data*

---

##  Why this project?

Financial institutions don’t ask *“How much can I gain?”*
They ask **“How much can I lose on a bad day?”**

This project answers that question using **Value at Risk (VaR)** — one of the most widely used risk metrics in **banks, hedge funds, and trading desks**.

---

## Concepts Applied

* Probability & statistics
* Quantiles & percentiles
* Monte Carlo simulation
* Financial risk modeling
* Data visualization

---

##  Tech Stack

| Tool       | Purpose               |
| ---------- | --------------------- |
| Python     | Core implementation   |
| pandas     | Data handling         |
| numpy      | Numerical computation |
| yfinance   | Market data           |
| matplotlib | Visualization         |

---

##  Data Source

* **Yahoo Finance**
* Time period: **Jan 2022 – Jan 2025**
* Frequency: **Daily**

---

##  Methodology (Simple Explanation)

### 🔹 Step 1: Data Collection

Historical stock prices are downloaded automatically using `yfinance`.

### 🔹 Step 2: Daily Returns

Daily returns are calculated using percentage change in prices.

### 🔹 Step 3: Historical VaR

* Uses **actual historical returns**
* 95% VaR = 5th percentile of returns
* Answers:

  > *“Based on the past, how bad can losses get?”*

### 🔹 Step 4: Monte Carlo VaR

* Simulates **10,000 future return scenarios**
* Assumes returns follow a normal distribution
* Answers:

  > *“If the future behaves statistically like the past, what is the risk?”*

### 🔹 Step 5: Visualization

* Histogram of returns
* Risk thresholds plotted clearly for comparison

---

## Results

| Metric              | Value        |
| ------------------- | ------------ |
| 95% Historical VaR  | ≈ **-2.02%** |
| 95% Monte Carlo VaR | ≈ **-2.33%** |

 **Interpretation:**
There is a **5% chance** that the stock may lose **more than ~2% in a single day**.

---

##  Future Enhancements

* Parametric (Variance–Covariance) VaR
* Expected Shortfall (CVaR)
* Portfolio-level VaR
* VaR backtesting

---




