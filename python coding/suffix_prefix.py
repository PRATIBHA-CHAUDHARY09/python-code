# Task 26: Write a program in Python that checks if a string starts with a given prefix or ends with a given suffix.
def check_prefix_suffix(s, prefix, suffix):
    starts_with = s.startswith(prefix)
    ends_with = s.endswith(suffix)
    return starts_with, ends_with

string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")
starts_with, ends_with = check_prefix_suffix(string, prefix, suffix)
print(f"Starts with {prefix}: {starts_with}")
print(f"Ends with {suffix}: {ends_with}")
