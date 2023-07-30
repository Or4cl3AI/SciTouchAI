```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class MachineLearningModel:
    def __init__(self, dataSet):
        self.dataSet = pd.read_csv(dataSet)
        self.model = RandomForestClassifier()

    def preprocess_data(self):
        # Assuming the last column is the target variable
        X = self.dataSet.iloc[:, :-1]
        y = self.dataSet.iloc[:, -1]

        # Splitting the dataset into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        return accuracy

    def processData(self):
        self.preprocess_data()
        self.train_model()
        accuracy = self.evaluate_model()
        return accuracy
```