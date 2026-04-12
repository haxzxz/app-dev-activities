from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        
        self.add_widget(Label(
            text = "My App Login",
            font_size = 32,
            size_hint = (1, 0.2)
        ))
        
        self.username = TextInput(
            hint_text = "Username",
            multiline = False,
            size_hint = (1, 0.1)
        )
        self.add_widget(self.username)
        
        self.password = TextInput(
            hint_text = "Password",
            password = True,
            multiline = False,
            size_hint = (1, 0.1)
        )
        self.add_widget(self.password)
        
        login_button = Button(
            text = "Login",
            size_hint=(1, 0.15)
        )
        login_button.bind(on_press = self.login)
        self.add_widget(login_button)
        
        register_button = Button(
            text="Register",
            size_hint=(1, 0.1)
        )
        
        register_button.bind(on_press=self.register)
        self,self.add_widget(register_button)
        
        self.message = Label(text = "")
        self.add_widget(self.message)
        
    def login(self, instance):
        if self.username.text == "admin" and self.password.text == "1234":
            self.message.text = "Login Successful"
        else:
            self.message.text = "Invalid Credentials"
    
    def register(self, instance):
        self.message.text = "Redirecting to Register Section"

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    MyApp().run()
        