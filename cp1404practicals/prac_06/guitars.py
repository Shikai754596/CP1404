from cp1404practicals.prac_06.guitar import Guitar

def main():
    print("My guitars!")
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
    name = input("Name: ")
    while name != "" and name.isspace() is False:
        year = input("Year: ")
        cost = input("Cost: ")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar)
        print()
        name = input("Name: ")

main()