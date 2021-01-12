from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKmApp(App):
    def build(self):
        Window.size = (600, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, miles, number):
        self.root.ids.input_number.text = miles + number


ConvertMilesKmApp().run()