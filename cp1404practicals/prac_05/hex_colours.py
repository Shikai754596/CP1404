def main():
    colour_code = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "BEIGE": "#f5f5dc",
                    "BLACK":  "#000000", "BLUEVIOLET":  "#8a2be2", "BROWN": "#a52a2a", "BURLYWOOD": "#deb887",
                    "CADETBLUE": "#5f9ea0", "CHOCOLATE": "#d2691e", "DARKGREEN": "#006400"}
    print(colour_code)

    colour_name = input("Enter a colour name: ").upper()
    while colour_name != "":
        if colour_name in colour_code:
            print(colour_name, "is", colour_code[colour_name])
        else:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").upper()


main()
