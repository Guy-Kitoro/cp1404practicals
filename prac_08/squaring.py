from kivy.app import App
from kivy.lang import Builder


class SquaringApp(App):
    """App to square a number."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Square Number"
        self.root = Builder.load_file("squaring.kv")
        return self.root

    def handle_calculate(self):
        """Calculate and display the square of the input number."""
        try:
            value = int(self.root.ids.input_number.text)
            self.root.ids.output_label.text = str(value ** 2)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"


if __name__ == '__main__':
    SquaringApp().run()
