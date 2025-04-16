📊 Steel Production Load Type Classification — Project Report
📌 Project Overview
This project aims to build a classification model that predicts the load type in a steel production process based on various process-related features. The dataset consists of 35,040 records and 11 columns containing information such as timestamps, process variables, and the target class Load_Type.

📑 Dataset Information
Total records: 35,040

Number of features: 11

Target variable: Load_Type (categorical)

)

🔧 Data Preprocessing
✅ Date-Time Feature Engineering
Converted the date column to Pandas DateTime using pd.to_datetime.

Extracted new features:

year

month

day

hour

minute

✅ Target Encoding
Mapped the Load_Type categories to numerical labels manually to avoid misencoding.

Used LabelEncoder to properly encode the target labels.

✅ Skewness Check & Scaling
Checked the skewness of numerical columns to decide on the appropriate scaling strategy.

Applied StandardScaler to numerical features.

Excluded the target variable Load_Type from scaling to avoid converting it to float values, which would cause the classifier to behave like a regressor.

Model Building
Performed train-test split using train_test_split.

Used a Random Forest Classifier for initial model training.

Evaluated model using:

Classification Report (accuracy, precision, recall, F1-score)

Confusion Matrix

Initial Results
Accuracy: ~40%

Visualized mistakes using ConfusionMatrixDisplay to identify class-wise errors.

Model Improvement
✅ Data Balancing
Applied SMOTE (Synthetic Minority Over-sampling Technique) to balance class distribution in the training set.

Retrained the Random Forest Classifier.

📈 Improved Results
Accuracy increased by 4%, improving from 40% to 44%.

Final confusion matrix and classification report confirmed a better balance in predictions across the target classes.

📌 Final Remarks
This project demonstrated the importance of:

Proper feature engineering (especially handling time-related features)

Careful preprocessing like scaling and encoding

Diagnosing class imbalance problems

Applying data balancing techniques like SMOTE

Iteratively evaluating and refining the model

Further improvements could include trying more advanced models (like XGBoost or LightGBM) and hyperparameter tuning for even better performance.
