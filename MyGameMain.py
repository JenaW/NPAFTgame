import kivy_venv
from kivy_venv.app import App
from kivy_venv.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()