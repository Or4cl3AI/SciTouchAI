```python
import json
from prototype.data_analysis import dataSet

def format_data(data):
    formatted_data = json.dumps(data, indent=4)
    return formatted_data

def present_data(formatted_data):
    print("Displaying data in a journalistic format:")
    print(formatted_data)

def renderUI():
    formatted_data = format_data(dataSet)
    present_data(formatted_data)

renderUI()
```