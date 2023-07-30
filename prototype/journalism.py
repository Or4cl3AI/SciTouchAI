```python
import json

def journalism():
    """
    This function incorporates principles of journalism into the application.
    It ensures that the data is presented in a clear, concise, and engaging manner.
    """
    with open('dataSet.json', 'r') as file:
        dataSet = json.load(file)

    # Sort data by relevance
    dataSet.sort(key=lambda x: x['relevance'], reverse=True)

    # Create headlines for top 5 most relevant data
    headlines = [f"Top {i+1}: {data['title']}" for i, data in enumerate(dataSet[:5])]

    # Create a summary for each headline
    summaries = [f"{data['summary'][:100]}..." for data in dataSet[:5]]

    # Combine headlines and summaries
    journalism_output = "\n".join([f"{headline}\n{summary}" for headline, summary in zip(headlines, summaries)])

    return journalism_output
```