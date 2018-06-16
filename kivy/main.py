from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
import kivy
kivy.require("1.10.0")

class HomePage(Screen):
	pass

class LoginScreen(Screen):
	pass

class SignUp(Screen):
	pass

class AboutPage(Screen):
	pass

class AudioFiles(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

presentation=Builder.load_file("main.kv")

class StellateApp(App):
	def build(self):
		return presentation

if __name__=="__main__":
	StellateApp().run()