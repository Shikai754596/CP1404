def main():

    

    number_file = open("numbers.txt", "r")
    number = 0
    for i in range(2):
        number += int(number_file.readline())
    print(number)


main()
