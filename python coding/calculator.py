# Task 24: Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
print(f"Result: {calculator(num1, num2, operator)}")
