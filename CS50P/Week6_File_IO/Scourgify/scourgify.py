import sys
import csv


def main():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a csv file")
    else:
        try:
            data = extract_data(sys.argv[1])
            write_data(sys.argv[2], data)
        except FileNotFoundError:
            sys.exit("File Not Found")


def extract_data(file_name):
    table = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last_name, first_name = row["name"].split(",")
            table.append(
                {
                    "first": first_name.lstrip(),
                    "last": last_name.lstrip(),
                    "house": row["house"],
                }
            )
    return table


def write_data(file_name, data):
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in data:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )


if __name__ == "__main__":
    main()
