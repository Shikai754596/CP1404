from cp1404practicals.prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
    name = input("Name: ")
    while name != "" and name.isspace() is False:
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar)
        print()
        name = input("Name: ")
    print("\n... snip ...\n")
    print("These are my guitars: ")
    for i, guitar in enumerate(guitars):
        if guitar.is_vintage() is False:
            vintage_string = ""
        else:
            vintage_string = "(vintage)"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string))

main()