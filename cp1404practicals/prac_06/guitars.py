from cp1404practicals.prac_06.guitar import Guitar

def main():
    print("My guitars!")
    name = input("Name: ")
    year = input("Year: ")
    cost = input("Cost: ")
    guitar = Guitar(name, year, cost)
    print(guitar)

main()