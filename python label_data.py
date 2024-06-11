import pandas as pd

# Load the dataset
data = pd.read_csv('processed_death_valley_weather.csv')

# Calculate the temperature difference for the next 3 hours (assuming hourly data)
data['TEMP_DIFF'] = data['TMIN'].shift(-3) - data['TMIN']

# Label the data: 1 if the temperature drop is significant (e.g., more than 5 degrees), else 0
data['LABEL'] = (data['TEMP_DIFF'] <= -5).astype(int)

# Save the labeled data to a new CSV file
data.to_csv('labeled_death_valley_weather.csv', index=False)

print("Data labeled and saved to 'labeled_death_valley_weather.csv'")
