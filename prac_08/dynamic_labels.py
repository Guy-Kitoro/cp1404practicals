from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App to dynamically display labels for a list of names."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and display labels dynamically."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


if __name__ == '__main__':
    DynamicLabelsApp().run()
