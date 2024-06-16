# Task 15: Write a program that reads data from a CSV file and prints it to the console.
import csv

def read_csv_file(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

read_csv_file("/Users/pratibhachaudhary/Downloads/machine-readable-business-employment-data-mar-2024-quarter.csv")
print( "csv file address: https://www.stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-March-2024-quarter/Download-data/business-employment-data-march-2024-quarter.zip")