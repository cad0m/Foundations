import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a csv file")
    else:
        try:
            print_table(sys.argv[1])
        except FileNotFoundError:
            sys.exit("File Not Found")


def print_table(file_name):
    table = []
    with open(file_name) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        print(tabulate(table[1:], table[0], tablefmt="grid"))


if __name__ == "__main__":
    main()
