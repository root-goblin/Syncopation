import kivy

kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.label import Label


class  SacrosanctApp(App):

	def build(self):
		return Label(text='Hello world')


if __name__ == '__main__':
	SacrosanctApp().run()