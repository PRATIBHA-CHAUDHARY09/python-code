# Task 18: Write a Python program that checks if two strings are anagrams of each other.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
print(f"Are the strings anagrams: {are_anagrams(string1, string2)}")
