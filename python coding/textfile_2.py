# Task 25: Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dst:
        dst.write(content)
    print(f"Contents copied from {source_file} to {destination_file}")

source_file = "/Users/pratibhachaudhary/Downloads/sample1.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)
