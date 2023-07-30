```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class MachineLearningModule:
    def __init__(self, data_set):
        self.data_set = data_set
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def preprocess_data(self):
        # Assuming the last column of the dataset is the target variable
        X = self.data_set.iloc[:, :-1]
        y = self.data_set.iloc[:, -1]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        self.model = RandomForestClassifier()
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        return accuracy

    def analyze_data(self):
        self.preprocess_data()
        self.train_model()
        accuracy = self.evaluate_model()
        return accuracy

if __name__ == "__main__":
    data_set = pd.read_csv('data_set.csv')
    ml_module = MachineLearningModule(data_set)
    accuracy = ml_module.analyze_data()
    print(f"Model Accuracy: {accuracy}")
```