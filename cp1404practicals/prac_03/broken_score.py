"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    if 100 < score < 0:
        print("Invalid score")
    elif 90 > score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    else:
        print("Bad")


main()
