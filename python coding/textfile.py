# Task 5: Write a program that takes a string input from the user and writes it to a text file.
def write_to_file(filename):
    user_input = input("Enter a string: ")
    with open(filename, 'w') as file:
        file.write(user_input)
    print(f"String written to {filename}")

write_to_file("output.txt")
