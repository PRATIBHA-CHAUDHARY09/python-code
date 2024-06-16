# Task 20: Write a Python program that takes a list of numbers and returns their sum.
def sum_of_list(numbers):
    return sum(numbers)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print(f"Sum of the numbers: {sum_of_list(numbers)}")
