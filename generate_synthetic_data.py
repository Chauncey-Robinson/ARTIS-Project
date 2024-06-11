import pandas as pd
from copulas.multivariate import GaussianMultivariate

# Load the dataset
file_path = 'death_valley_weather.csv'
data = pd.read_csv(file_path)

# Inspect the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Inspect the data summary
print("\nData summary:")
print(data.info())

# Preprocess the data by removing non-numeric columns
numeric_data = data.drop(columns=['STATION', 'NAME', 'DATE'])

# Fill NaN values with the mean of their respective columns
numeric_data = numeric_data.apply(lambda x: x.fillna(x.mean()), axis=0)

# Check if NaN values have been handled
print("\nData after handling NaN values:")
print(numeric_data.info())

# Generate synthetic data
model = GaussianMultivariate()
model.fit(numeric_data)

# Sample synthetic data
synthetic_data = model.sample(len(data))

# Save the synthetic data to a new CSV file
synthetic_data.to_csv('synthetic_death_valley_weather.csv', index=False)

print("\nSynthetic data saved to 'synthetic_death_valley_weather.csv'")
