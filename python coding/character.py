# Task 16: Write a program in Python that counts the frequency of each character in a string.
def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

user_input = input("Enter a string: ")
print(f"Character frequency: {char_frequency(user_input)}")
