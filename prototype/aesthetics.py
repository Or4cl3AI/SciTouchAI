import matplotlib.pyplot as plt
from matplotlib import style

# Shared variable
dataSet = None

def renderUI():
    global dataSet

    # Set the style of the visualization
    style.use('ggplot')

    # Create a new figure for the visualization
    plt.figure(figsize=(10, 6))

    # Plot the data
    plt.plot(dataSet)

    # Set the title and labels
    plt.title('Scientific Data Analysis')
    plt.xlabel('Data Points')
    plt.ylabel('Values')

    # Show the plot
    plt.show()

def setDataSet(data):
    global dataSet
    dataSet = data

def getDataSet():
    global dataSet
    return dataSet