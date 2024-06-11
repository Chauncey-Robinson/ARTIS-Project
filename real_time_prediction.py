import pandas as pd
import joblib
from sklearn.impute import SimpleImputer

# Load the trained model
model = joblib.load('trained_model.pkl')

# Load the new data
new_data = pd.read_csv('new_data.csv')

# Handle missing values in the new data
imputer = SimpleImputer(strategy='mean')
new_data_imputed = imputer.fit_transform(new_data)

# Make predictions
predictions = model.predict(new_data_imputed)

# Output the predictions
print("Predictions for the new data:")
print(predictions)
