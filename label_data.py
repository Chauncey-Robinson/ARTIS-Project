import pandas as pd

# Load the dataset
data = pd.read_csv('death_valley_weather.csv')

# Ensure that the dates are in datetime format
data['DATE'] = pd.to_datetime(data['DATE'])

# Sort data by date to ensure chronological order
data = data.sort_values(by='DATE')

# Calculate the temperature difference between consecutive days
data['TEMP_DIFF'] = data['TMAX'].diff(periods=1)

# Label the data where the temperature drop is greater than or equal to 10 degrees
data['LABEL'] = (data['TEMP_DIFF'] <= -10).astype(int)

# Save the labeled dataset
data.to_csv('labeled_death_valley_weather.csv', index=False)

print("Data labeled and saved to 'labeled_death_valley_weather.csv'")
import pandas as pd

# Load the dataset
data = pd.read_csv('death_valley_weather.csv')

# Ensure that the dates are in datetime format
data['DATE'] = pd.to_datetime(data['DATE'])

# Sort data by date to ensure chronological order
data = data.sort_values(by='DATE')

# Calculate the temperature difference between consecutive days
data['TEMP_DIFF'] = data['TMAX'].diff(periods=1)

# Label the data where the temperature drop is greater than or equal to 10 degrees
data['LABEL'] = (data['TEMP_DIFF'] <= -10).astype(int)

# Save the labeled dataset
data.to_csv('labeled_death_valley_weather.csv', index=False)

print("Data labeled and saved to 'labeled_death_valley_weather.csv'")
