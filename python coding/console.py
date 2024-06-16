# Task 6: Write a program that reads the content of a text file and prints it to the console.
def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)

read_from_file("output.txt")
