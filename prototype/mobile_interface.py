import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from prototype.data_analysis import analyzeData
from prototype.touchscreen_input import touchInput
from prototype.human_computer_interaction import HCI
from prototype.natural_language_processing import NLP

kivy.require('1.0.9')

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.loginButton = Button(text="Login")
        self.loginButton.bind(on_press=self.authenticateUser)
        self.add_widget(self.loginButton)

    def authenticateUser(self, instance):
        username = self.username.text
        password = self.password.text
        # Call the authenticateUser function from the authentication.py file
        isAuthenticated = authenticateUser(username, password)
        if isAuthenticated:
            self.add_widget(Label(text='Login Successful'))
        else:
            self.add_widget(Label(text='Login Failed'))

class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()