```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Shared variable
dataSet = None

# Shared schema
dataSetSchema = None

def load_data(file_path):
    global dataSet
    dataSet = pd.read_csv(file_path)
    validate_data()

def validate_data():
    global dataSetSchema
    if dataSetSchema is not None:
        assert set(dataSet.columns) == set(dataSetSchema), "Data does not match the schema"

def preprocess_data():
    global dataSet
    scaler = StandardScaler()
    dataSet = pd.DataFrame(scaler.fit_transform(dataSet), columns=dataSet.columns)

def processData():
    load_data('path_to_your_data.csv')
    preprocess_data()
    print("Data processed successfully")
    return "dataProcessed"

if __name__ == "__main__":
    processData()
```