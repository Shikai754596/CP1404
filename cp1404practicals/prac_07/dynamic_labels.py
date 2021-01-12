from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()
    
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_list = ["Bob Brown", "Cat Cyan", "Oren Ochre", "John Wick", "Jack Watson"]

    def build(self):
        Window.size = (600, 200)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self):
        for name in self.name_list:
            temp_button = Button(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_button)