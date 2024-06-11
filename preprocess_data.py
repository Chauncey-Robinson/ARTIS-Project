import pandas as pd

# Load the data
file_path = '~/Desktop/artis_env/processed_death_valley_weather.csv'
data = pd.read_csv(file_path)

# Check for missing values and handle them
data.fillna(method='ffill', inplace=True)

# Feature engineering: Create temperature gradient
data['TEMP_GRADIENT'] = data['TMAX'] - data['TMIN']

# Save the preprocessed data
data.to_csv('preprocessed_death_valley_weather.csv', index=False)

# Display summary
print(data.info())
print(data.head())
