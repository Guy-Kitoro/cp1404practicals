from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemoApp(App):
    """App to demonstrate BoxLayout with Greet and Clear functionality."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file("box_layout.kv")
        return self.root

    def handle_greet(self):
        """Greet the user by updating the label with their name."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}!"

    def handle_clear(self):
        """Clear the text input and label."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


if __name__ == '__main__':
    BoxLayoutDemoApp().run()
