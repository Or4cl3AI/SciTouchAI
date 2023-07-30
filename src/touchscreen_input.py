```python
import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TouchScreenInputApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.inputField = TextInput(multiline=False)
        self.inputField.bind(on_text_validate=self.on_enter)
        layout.add_widget(self.inputField)
        return layout

    def on_enter(self, instance):
        userInput = instance.text
        instance.text = ''
        self.processUserInput(userInput)

    def processUserInput(self, userInput):
        # This function will process the user input and pass it to the relevant functions
        # For now, it just prints the input to the console
        print(f"User input: {userInput}")

if __name__ == '__main__':
    TouchScreenInputApp().run()
```