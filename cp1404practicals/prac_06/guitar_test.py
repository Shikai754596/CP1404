from cp1404practicals.prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013)

    print("{} get_age() - Excepted 98. Got {}".format(gibson.name, gibson.get_age()))
    print("{} get_age() - Excepted 7. Got {}".format(another.name, another.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(another.name, another.is_vintage()))
    print("{} is_vintage() - Expected True. Got {}".format(another.name, another.is_vintage()))


main()
