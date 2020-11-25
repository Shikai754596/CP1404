def main():
    name = input("Please enter your name: ")
    name_input_file = open("name.txt", "w")
    print(name, file=name_input_file)
    name_input_file.close()

    name_output_file = open("name.txt", "r")
    print("Your name is {}".format(name_output_file.read()))

    number_file = open("numbers.txt", "r")
    number = 0
    for i in range(2):
        number += int(number_file.readline())
    print(number)

    number_file = open("numbers.txt", "r")
    number = 0
    for line_number in number_file:
        number += int(line_number)
    print(number)


main()
