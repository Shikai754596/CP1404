"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(score_checker(score))


def score_checker(scores):
    """ Return the result of different scores"""
    if 100 < scores < 0:
        return "Invalid score"
    if 100 < scores < 0:
        return "Invalid score"
    elif 90 > scores >= 50:
        return "Passable"
    elif scores >= 90:
        return "Excellent"
    else:
        return "Bad"


main()
