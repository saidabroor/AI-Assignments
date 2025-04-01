**Gold Price Prediction Using Machine Learning**

In my this project, I built a predictive model to estimate gold prices using historical financial data. The dataset consists of **3,904 entries** with **47 features**, including major stock indices (S&P 500, Nasdaq), interest rates, CPI, forex pairs, and other commodities like silver and gold.

**Meaning of the columns:**
S&P - Standard & Poor's 500 stock market
Nasdaq - electronic stock exchange market
open - opening price
high - highest price
low - lowest price

### **Data Preprocessing & Feature Engineering**

- Utilized `klib` for data cleaning and correlation analysis.
- Handled missing values appropriately for a more robust model.
- Target variable: **Gold High** price.

# **Model Training & Hyperparameter Tuning**

I trained three powerful gradient-boosting models using **RandomizedSearchCV** for hyperparameter optimization:

| Model    | MSE         | R² Score |
| -------- | ----------- | -------- |
| LightGBM | 0.000623065 | 0.999448 |
| GBM      | 0.000214354 | 0.999810 |
| XGBoost  | 0.000546282 | 0.999516 |

### **Key Findings**

**GBM outperformed the other models**, achieving the lowest MSE (0.000214354) and the highest R² score (0.99981), indicating near-perfect predictions.

**XGBoost and LightGBM also performed well**, proving the effectiveness of gradient boosting algorithms for financial time series forecasting.
