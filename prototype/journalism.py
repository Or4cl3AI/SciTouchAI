```python
import json
from prototype.data_analysis import data_set

class Journalism:
    def __init__(self):
        self.data_set = data_set

    def create_story(self):
        story = {}
        for data in self.data_set:
            story[data['name']] = self.analyze_data(data)
        return story

    def analyze_data(self, data):
        analysis = {}
        analysis['title'] = self.create_title(data)
        analysis['content'] = self.create_content(data)
        return analysis

    def create_title(self, data):
        return f"Analysis of {data['name']}"

    def create_content(self, data):
        content = f"The data set {data['name']} has {len(data['values'])} values. "
        content += f"The average value is {sum(data['values'])/len(data['values'])}. "
        content += f"The maximum value is {max(data['values'])}. "
        content += f"The minimum value is {min(data['values'])}. "
        return content

journalism = Journalism()
print(json.dumps(journalism.create_story(), indent=4))
```