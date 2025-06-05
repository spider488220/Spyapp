from kivy.app import App
from kivy.uix.label import Label

class SpyApp(App):
    def build(self):
        return Label(text="Hello from SpyApp!")

if __name__ == "__main__":
    SpyApp().run()
  
