```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Shared variables
data_set = None
user_input = None

def load_data(file_path):
    global data_set
    data_set = pd.read_csv(file_path)

def preprocess_data():
    global data_set
    # Standardize the data
    scaler = StandardScaler()
    data_set = scaler.fit_transform(data_set)

def analyze_data():
    global data_set
    # Apply PCA for dimensionality reduction
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data_set)
    data_set = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

def save_results(file_path):
    global data_set
    data_set.to_csv(file_path, index=False)

def run_data_analysis(input_file, output_file):
    load_data(input_file)
    preprocess_data()
    analyze_data()
    save_results(output_file)
    print("Data_Analysis_Complete")
```