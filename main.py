from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class myLayout(BoxLayout):
	def __init__(self, *args, **kwargs):
		# super(myLayout, self).__init__(**kwargs)
		super().__init__()
		self.orientation="vertical"
		self.b1= BoxLayout()
		self.b1.add_widget(Label(text="Label1"))
		self.b1.add_widget(Label(text="Label2"))
		self.b1.add_widget(Label(text="Label3"))
		self.b1.add_widget(Label(text="Label4"))
		
		self.add_widget(self.b1)
		btn = Button(text="remove")
		btn.bind(on_press=self.removeWidgget)
		self.add_widget(btn)

	def removeWidgget(self, instance):
		#print(self.b1.children[0].text)
		self.b1.remove_widget(self.b1.children[0])

class MyBox(App):
	def build(self):
		return myLayout()
		
if __name__=='__main__':
	MyBox().run()
