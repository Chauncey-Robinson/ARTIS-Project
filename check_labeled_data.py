import pandas as pd

# Load the labeled dataset
data = pd.read_csv('labeled_death_valley_weather.csv')

# Print the first few rows and columns
print("First few rows of the labeled dataset:")
print(data.head())

print("\nColumns in the dataset:")
print(data.columns)
