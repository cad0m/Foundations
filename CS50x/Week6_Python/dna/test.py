import csv
import sys


with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames[1:]
DNAtext = open(sys.argv[2], "r")
text = DNAtext.read()
print(header)

