# Task 27: Write a program in Python that converts a string into a list of its characters.
def string_to_char_list(s):
    return list(s)

string = input("Enter a string: ")
print(f"List of characters: {string_to_char_list(string)}")
