from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKmApp(App):
    """App to convert miles to kilometers."""
    result_text = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.result_text = "0.0 km"
        return self.root

    def handle_convert(self):
        """Convert miles to kilometers."""
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * 1.60934
            self.result_text = f"{kilometers:.3f} km"
        except ValueError:
            self.result_text = "Invalid input"

    def handle_increment(self, increment):
        """Increment the miles input by the given value."""
        try:
            current_value = float(self.root.ids.input_miles.text)
        except ValueError:
            current_value = 0
        self.root.ids.input_miles.text = str(current_value + increment)
        self.handle_convert()


if __name__ == '__main__':
    ConvertMilesKmApp().run()
