import random


def main():
    lines = int(input("How many quick picks? "))
    CONSTANTS = []
    number_lines = []
    for i in range(lines):
        for t in range(5):
            number_lines += [random.randint(1, 45)]
        CONSTANTS.append(number_lines)
        for number in CONSTANTS[i]:
            print(number, end=" ")
        print()





main()
