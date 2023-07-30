```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Importing the data set
data_set = pd.read_csv('data_set.csv')

# Function to analyze data
def analyzeData(data_set):
    # Splitting the data into features and target
    X = data_set.drop('target', axis=1)
    y = data_set['target']

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Creating the model
    model = RandomForestClassifier(n_estimators=100)

    # Training the model
    model.fit(X_train, y_train)

    # Making predictions
    predictions = model.predict(X_test)

    # Checking the accuracy
    accuracy = accuracy_score(y_test, predictions)

    return accuracy

# Running the function
analyzeData(data_set)
```