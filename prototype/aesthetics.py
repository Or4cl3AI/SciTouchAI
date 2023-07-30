```python
import matplotlib.pyplot as plt
from prototype.responsive_design import optimizeDisplay

def applyAesthetics(data_set):
    plt.style.use('seaborn-darkgrid')
    plt.rcParams['figure.figsize'] = [10, 5]

    # Apply aesthetics to the data set
    for data in data_set:
        plt.plot(data)
        plt.title('Scientific Data Analysis')
        plt.xlabel('Data Points')
        plt.ylabel('Values')

    # Call the function from responsive_design.py to optimize the display
    optimizeDisplay()

    plt.show()

def enhanceAesthetics(user_input):
    # Apply aesthetics to the user interface based on the user input
    if user_input == 'dark':
        plt.style.use('dark_background')
    elif user_input == 'light':
        plt.style.use('seaborn-whitegrid')
    else:
        plt.style.use('classic')

    # Call the function from responsive_design.py to optimize the display
    optimizeDisplay()

    plt.show()
```