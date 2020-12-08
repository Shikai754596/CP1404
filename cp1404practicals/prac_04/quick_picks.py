import random


def main():
    lines = int(input("How many quick picks? "))
    CONSTANTS = []
    for i in range(lines):
        number_lines = []
        for t in range(6):
            number_lines += [random.randint(1, 45)]
        CONSTANTS.append(number_lines)
        for number in CONSTANTS[i]:
            print("{:2}".format(number), end=" ")
        print()


main()
