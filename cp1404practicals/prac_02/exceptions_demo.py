"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Cannot divide by zero, please enter again: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# When the input value is string instead of a number.
# When will a ZeroDivisionError occur?
# When dominator == 0.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes