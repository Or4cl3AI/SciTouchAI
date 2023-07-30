```python
from src.user_interface import dataDisplay

class JournalismPrinciples:
    def __init__(self):
        self.story_structure = []
        self.visual_elements = []

    def apply_journalism_principles(self, dataSet):
        self.story_structure = self.create_story_structure(dataSet)
        self.visual_elements = self.create_visual_elements(dataSet)
        self.update_interface()

    def create_story_structure(self, dataSet):
        # Analyze the data set and create a story structure
        # This is a placeholder and should be replaced with actual implementation
        return ["Introduction", "Body", "Conclusion"]

    def create_visual_elements(self, dataSet):
        # Analyze the data set and create visual elements
        # This is a placeholder and should be replaced with actual implementation
        return ["Graph", "Chart", "Image"]

    def update_interface(self):
        # Update the user interface with the story structure and visual elements
        dataDisplay.update(self.story_structure, self.visual_elements)

def applyJournalismPrinciples(dataSet):
    journalism = JournalismPrinciples()
    journalism.apply_journalism_principles(dataSet)
```
