```python
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class TouchScreenInput(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.inputField = TextInput(hint_text='Enter your data here')
        self.submitButton = Button(text='Submit', on_press=self.analyzeData)
        layout.add_widget(self.inputField)
        layout.add_widget(self.submitButton)
        return layout

    def analyzeData(self, instance):
        userInput = self.inputField.text
        # Call the analyzeData function from data_analysis.py
        from data_analysis import analyzeData
        analyzedData = analyzeData(userInput)
        # Display the analyzed data
        self.displayData(analyzedData)

    def displayData(self, analyzedData):
        # Call the displayData function from app.py
        from app import displayData
        displayData(analyzedData)

if __name__ == '__main__':
    TouchScreenInput().run()
```