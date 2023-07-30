import pandas as pd
from sklearn.preprocessing import StandardScaler

# Importing the schema for scientific data
from src.schemas import ScientificDataSchema

# Variable for the scientific data set
dataSet = None

def load_data(file_path):
    """
    Function to load the scientific data set from a given file path.
    """
    global dataSet
    dataSet = pd.read_csv(file_path)
    validate_data(dataSet)

def validate_data(data):
    """
    Function to validate the scientific data set against the ScientificDataSchema.
    """
    schema = ScientificDataSchema()
    errors = schema.validate(data)
    if errors:
        raise ValueError(f"Data validation errors: {errors}")

def preprocess_data():
    """
    Function to preprocess the scientific data set.
    """
    global dataSet
    # Standardizing the data
    scaler = StandardScaler()
    dataSet = scaler.fit_transform(dataSet)

def processData():
    """
    Function to process the scientific data set.
    """
    preprocess_data()
    # Send a message that the data has been processed
    print("dataProcessed")