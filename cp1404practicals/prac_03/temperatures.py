"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def cel_to_fah(cel):
    """Convert celsius to fahrenheit"""
    fah = cel * 9.0 / 5 + 32
    return fah


def fah_to_cel(fah):
    """Convert fahrenheit to celsius"""
    cel = (fah - 32) * 5 / 9
    return cel


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = cel_to_fah(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fah_to_cel(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
