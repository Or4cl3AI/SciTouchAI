```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the scientific data set
def load_data():
    dataSet = pd.read_csv('dataSet.csv')
    return dataSet

# Preprocess the data
def preprocess_data(dataSet):
    # Assuming the last column is 'target'
    X = dataSet.iloc[:, :-1]
    Y = dataSet.iloc[:, -1]
    return X, Y

# Split the data into training and testing sets
def split_data(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)
    return X_train, X_test, Y_train, Y_test

# Train the model
def train_model(X_train, Y_train):
    model = RandomForestClassifier()
    model.fit(X_train, Y_train)
    return model

# Test the model
def test_model(model, X_test, Y_test):
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    return accuracy

# Main function to control the flow
def main():
    dataSet = load_data()
    X, Y = preprocess_data(dataSet)
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    model = train_model(X_train, Y_train)
    accuracy = test_model(model, X_test, Y_test)
    print(f'Model Accuracy: {accuracy}')

if __name__ == "__main__":
    main()
```