"""
CP1404/CP5632 Practical
Hex colour lookup program
"""

HEX_COLOURS = {
    "AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff",
    "Azure": "#f0ffff", "Beige": "#f5f5dc", "Black": "#000000",
    "BlueViolet": "#8a2be2", "Brown": "#a52a2a", "BurlyWood": "#deb887",
    "CadetBlue": "#5f9ea0"
}


def main():
    """Lookup hex colour codes based on user input."""
    colour_name = input("Enter a colour name: ").strip()
    while colour_name != "":
        hex_code = HEX_COLOURS.get(colour_name.title())
        if hex_code:
            print(f"{colour_name.title()} has hex code {hex_code}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").strip()


main()
