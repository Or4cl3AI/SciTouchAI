```python
import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

dataSet = None
userInput = None

class TouchScreenInputApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        self.userInput = TextInput(multiline=False)
        submitButton = Button(text="Submit")
        submitButton.bind(on_press=self.submit_input)
        layout.add_widget(self.userInput)
        layout.add_widget(submitButton)
        return layout

    def submit_input(self, instance):
        global userInput
        userInput = self.userInput.text
        self.userInput.text = ""

if __name__ == "__main__":
    TouchScreenInputApp().run()
```