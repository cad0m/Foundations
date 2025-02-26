import sys

def main():
    if len(sys.argv) != 2:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        else:
            sys.exit("Too few command-line arguments")
    elif sys.argv[1][-3:] != ".py":
            sys.exit("not a python file")
    else:
        try:
            print(count_lines(sys.argv[1]))
        except FileNotFoundError:
            sys.exit("Not a Python file")

def count_lines(file_name):
    count = 0
    with open(file_name) as file:
        for line in file:
            striped_line = line.strip()
            if striped_line and not striped_line.startswith('#') :
                count += 1
    return count

if __name__ == "__main__":
    main()


