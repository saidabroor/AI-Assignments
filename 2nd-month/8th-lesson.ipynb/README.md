Project Report: Predicting Target Death Rate

1. Introduction

The objective of this project is to develop a regression model to predict the target death rate using a dataset containing 3,047 entries and 33 features. The dataset includes various demographic, economic, and healthcare-related indicators that could influence mortality rates.

2. Data Preprocessing

- Handling Missing Values:
  - Numerical features with missing values were imputed using the mode and mean (for continuous data) to maintain consistency and prevent data loss.
  - Categorical features with missing values were imputed using the mode.
- Encoding Categorical Variables:
  - Label Encoding was applied to ordinal categorical variables.
  - One-Hot Encoding was used for nominal categorical variables to ensure proper model learning.
- Feature Scaling:
  - StandardScaler was applied to numerical features to normalize the range of values and improve model efficiency.

3. Model Selection and Evaluation
   The following regression models were trained and evaluated using Mean Squared Error (MSE) and R-squared (R²) scores:

| Model                 | MSE  | R² Score |
| --------------------- | ---- | -------- |
| RandomForestRegressor | 0.47 | 0.56     |
| DecisionTreeRegressor | 0.67 | 0.37     |
| LinearRegression      | 0.51 | 0.52     |
| LGBMRegressor         | 0.33 | 0.69     |

4. Results Analysis

- Performance metrics such as mse and r2 score analyzed to determine which model best predicts the target death rate.
- LGBMRegressor could be effective if tuned properly, given its ability to handle large datasets efficiently.

5. Conclusion and Future Improvements

- Feature Engineering: Additional feature creation and transformations may improve predictive power.

- Hyperparameter Tuning: Optimizing hyperparameters, especially for ensemble models, could enhance performance.

- Ensemble Learning: Combining multiple models through stacking or boosting may yield better results.
