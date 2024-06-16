# Task 17: Write a program in Python that converts a given string to title case (first letter of each word capitalized).
def to_title_case(s):
    return s.title()

user_input = input("Enter a string: ")
print(f"Title case string: {to_title_case(user_input)}")
