import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.impute import SimpleImputer

# Load the labeled dataset
data = pd.read_csv('labeled_death_valley_weather.csv')

# Remove non-numeric columns
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
numeric_columns.remove('LABEL')  # Ensure LABEL is not removed
features = data[numeric_columns]

# Handle missing values by filling them with the median value
imputer = SimpleImputer(strategy='median')
features = imputer.fit_transform(features)

# Target variable
target = data['LABEL']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))
