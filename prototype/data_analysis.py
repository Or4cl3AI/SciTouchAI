import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def analyzeData(dataSet):
    # Load the dataset
    data = pd.read_csv(dataSet)

    # Standardize the data
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    # Apply PCA
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)

    # Convert to dataframe
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

    return principalDf