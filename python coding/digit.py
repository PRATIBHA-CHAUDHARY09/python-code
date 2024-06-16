# Task 12: Write a Python program that calculates the sum of the digits of a given number.
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

number = int(input("Enter a number: "))
print(f"Sum of the digits: {sum_of_digits(number)}")

