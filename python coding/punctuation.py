# Task 19: Write a Python program that removes all punctuation from a given string.
import string

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

user_input = input("Enter a string: ")
print(f"String without punctuation: {remove_punctuation(user_input)}")
