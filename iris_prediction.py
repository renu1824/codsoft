# -*- coding: utf-8 -*-
"""iris prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tT23-uhBVYhNbcL9O2mWv5PGcv1Po1KZ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
# Load the dataset (Assume CSV file is provided)
# Specify the encoding as 'latin-1' or 'ISO-8859-1'
data = pd.read_csv('/content/IMDb Movies India.csv', encoding='latin-1')  # Replace with the actual path to your dataset
print(data.head())  # Check the first few rows of the dataset
# Handle missing values for categorical features (e.g., fill with 'Unknown')
data['Genre'] = data['Genre'].fillna('Unknown')
data['Director'] = data['Director'].fillna('Unknown')
data['Actor 1'] = data['Actor 1'].fillna('Unknown')
data['Actor 2'] = data['Actor 2'].fillna('Unknown')
data['Actor 3'] = data['Actor 3'].fillna('Unknown')
data['Rating'] = data['Rating'].fillna(data['Rating'].median())  # Impute missing Rating with median

# Check for any remaining missing values
print(data.isnull().sum())
# Select features (X) and target variable (y)
X = data[['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']]  # Using categorical columns as features
y = data['Rating']  # Rating is the target variable
# Split the data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a column transformer for one-hot encoding the categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3'])
    ])

# Create a pipeline with preprocessing and a regression model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model on the training data
model.fit(X_train, y_train)
# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Optionally, plot the predicted vs actual ratings
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Ratings')
plt.ylabel('Predicted Ratings')
plt.title('Actual vs Predicted Ratings')# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset (taking the CSV file path as user input)
file_path = input("Please enter the path to the Iris dataset CSV file: ")

# Read the dataset into a pandas DataFrame
data = pd.read_csv('/content/IRIS.csv')

# Step 2: Check for missing values
print(data.isnull().sum())  # Check for missing values in each column

# Step 3: Preprocess the data
# Encode the 'species' column (target variable) into numeric values
label_encoder = LabelEncoder()
data['species'] = label_encoder.fit_transform(data['species'])

# Step 4: Split the dataset into features (X) and target (y)
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Features
y = data['species']  # Target variable

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Feature scaling (Optional, but often improves model performance)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # Fit and transform the training data
X_test = scaler.transform(X_test)  # Only transform the test data

# Step 6: Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: Make predictions
y_pred = model.predict(X_test)

# Step 8: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')

# Display the classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

# Step 9: Use the model to make predictions on new data (Example input)
# Example: Predicting the species for a new flower with specific measurements
new_data = [[5.1, 3.5, 1.4, 0.2]]  # Example feature values (sepal_length, sepal_width, petal_length, petal_width)
new_data_scaled = scaler.transform(new_data)  # Scale the new data using the same scaler
prediction = model.predict(new_data_scaled)
predicted_species = label_encoder.inverse_transform(prediction)  # Convert numeric prediction back to species name
print(f"Predicted species for the new flower: {predicted_species[0]}")

plt.show()
# Example: Predicting ratings for new movies
new_movies = pd.DataFrame({
    'Genre': ['Action', 'Comedy'],
    'Director': ['Director1', 'Director2'],
    'Actor 1': ['Actor1', 'Actor2'],
    'Actor 2': ['Actor3', 'Actor4'],
    'Actor 3': ['Actor5', 'Actor6']
})

# Predict the ratings for the new movies
new_predictions = model.predict(new_movies)
print(new_predictions)