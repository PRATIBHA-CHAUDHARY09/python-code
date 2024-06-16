# Task 14: Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
def read_multiple_lines():
    lines = []
    while True:
        line = input("enter your lines")
        if line == "":
            break
        lines.append(line)
    return lines

lines = read_multiple_lines()
print("You entered:")
for line in lines:
    print(line)
