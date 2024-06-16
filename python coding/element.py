# Task 21: Write a Python program that counts the occurrences of a specific element in a list.
def count_occurrences(lst, element):
    return lst.count(element)

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
print(f"Occurrences of {element}: {count_occurrences(numbers, element)}")
