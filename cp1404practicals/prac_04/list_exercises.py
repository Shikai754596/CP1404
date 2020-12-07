def main():
    numbers = get_numbers(5)
    numbers_calculation(numbers)


def get_numbers(times):
    """Get several numbers from user and output a list of these numbers"""
    number_list = []
    for i in range(times):
        number_list += [int(input("Number: "))]
    return number_list


def numbers_calculation(number_list):
    """Calculate and print numbers from the list as requested"""
    first_number = number_list[0]
    last_number = number_list[-1]
    smallest_number = min(number_list)
    largest_number = max(number_list)
    average_number = sum(number_list) / len(number_list)
    print("The first number is {}".format(first_number))
    print("The last number is {}".format(last_number))
    print("The smallest number is {}".format(smallest_number))
    print("The largest number is {}".format(largest_number))
    print("The average of the numbers is {}".format(average_number))


main()
