---

# 📉 Value at Risk (VaR) Analysis using Python

*A practical risk-management project using real stock market data*

---

## 🔍 Why this project?

Financial institutions don’t ask *“How much can I gain?”*
They ask **“How much can I lose on a bad day?”**

This project answers that question using **Value at Risk (VaR)** — one of the most widely used risk metrics in **banks, hedge funds, and trading desks**.

---

## 🚀 What this project does

✔️ Downloads **real stock market data**
✔️ Calculates **daily returns**
✔️ Estimates **95% downside risk**
✔️ Compares **Historical vs Monte Carlo VaR**
✔️ Visualizes risk clearly with plots

📌 Stock analyzed: **Reliance Industries (RELIANCE.NS)**

---

## 🧠 Concepts Applied

* Probability & statistics
* Quantiles & percentiles
* Monte Carlo simulation
* Financial risk modeling
* Data visualization

---

## 🛠️ Tech Stack

| Tool       | Purpose               |
| ---------- | --------------------- |
| Python     | Core implementation   |
| pandas     | Data handling         |
| numpy      | Numerical computation |
| yfinance   | Market data           |
| matplotlib | Visualization         |

---

## 📊 Data Source

* **Yahoo Finance**
* Time period: **Jan 2023 – Jan 2025**
* Frequency: **Daily**

---

## 🧮 Methodology (Simple Explanation)

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

## 📈 Results

| Metric              | Value        |
| ------------------- | ------------ |
| 95% Historical VaR  | ≈ **-2.02%** |
| 95% Monte Carlo VaR | ≈ **-2.33%** |

📌 **Interpretation:**
There is a **5% chance** that the stock may lose **more than ~2% in a single day**.

---

## 📊 Visualization

The plot below shows:

* Distribution of daily returns
* Historical VaR (red line)
* Monte Carlo VaR (green line)

📁 Saved as: `var_distribution.png`

---

## 📂 Project Structure

```
VaR_Project/
│
├── var_model.py              # Main VaR implementation
├── RELIANCE.csv              # Price data
├── daily_returns.csv         # Computed returns
├── var_distribution.png      # Visualization
└── README.md                 # Documentation
```

---

## ▶️ How to Run

```bash
pip install yfinance pandas numpy matplotlib
python var_model.py
```

---

## 🎯 Why this project matters?

This project demonstrates:

* ✅ Ability to work with **real financial data**
* ✅ Understanding of **risk metrics used in industry**
* ✅ Hands-on **quantitative modeling**
* ✅ Clean visualization & interpretation
* ✅ End-to-end project ownership

---

## 🔮 Future Enhancements

* Parametric (Variance–Covariance) VaR
* Expected Shortfall (CVaR)
* Portfolio-level VaR
* VaR backtesting

---




Just tell me 💙
