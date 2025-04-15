# **Wine Quality Prediction Report**

**Project overview**

This project focuses on predicting the quality of wine based on various physicochemical properties using a Decision Tree Regressor. The original dataset consisted of 1,145 rows and 12 columns.

**Data Cleaning & Preprocessing**

Removed non-numeric values: Cleaned out any string or text-type entries in numeric columns.
Handled missing values:

- Used mean imputation for numeric columns.
- Used mode imputation for categorical/text-based columns (if any).

**Feature Engineering & Selection**

- Created 5 new feature columns to enhance the model's predictive ability.
- Applied Mutual Information (MI) to measure the contribution of each feature to the target variable.
- Based on MI scores, removed 4 features that had very low contribution to the prediction outcome.

**Scaling**

- Checked the skewness of each feature:
- Normally distributed columns → scaled using **StandardScaler**.
- Skewed columns / outlier-heavy → scaled using **RobustScaler**.

**Model Training**

Trained a Decision Tree Regressor and Random Forest Regressor on the processed dataset.
Used metrics such as Mean_squared_error and R2_score
Evaluated the model performance using:
K-Fold Cross-Validation (5 splits, shuffled, random state 42)
Calculated mean and standard deviation of the cross-validation scores for reliable performance estimation.

**Summary and result**
Successfully cleaned and preprocessed the dataset.
Mse has been 0.24 and r2 was 0.46 at the final result.
Performed feature engineering and selection to improve model accuracy.
Applied appropriate scaling techniques based on distribution analysis.
Validated the model using K-Fold Cross-Validation to check consistency and generalization ability.
