```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load the dataset
def load_data(dataSet):
    data = pd.read_csv(dataSet)
    return data

# Preprocess the data
def preprocess_data(data):
    X = data.drop('target', axis=1)
    y = data['target']
    
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y

# Split the data into training and testing sets
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Train the model
def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Main function to process the data
def processData(dataSet):
    data = load_data(dataSet)
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    
    print(f'Model Accuracy: {accuracy}')
    return model
```