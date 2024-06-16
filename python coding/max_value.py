# Task 22: Write a Python program that returns the minimum and maximum values in a list of numbers.
def min_and_max(lst):
    return min(lst), max(lst)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
minimum, maximum = min_and_max(numbers)
print(f"Minimum value: {minimum}")
print(f"Maximum value: {maximum}")
