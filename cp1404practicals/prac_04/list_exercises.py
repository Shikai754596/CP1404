def main():
    numbers = get_numbers(5)


def get_numbers(times):
    number_list = []
    for i in range(times):
        number_list += [int(input("Number: "))]
    return number_list


main()
