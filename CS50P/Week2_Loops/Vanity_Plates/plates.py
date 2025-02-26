def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    condition = True
    found_digit = False
    if not 2 <= len(s) <= 6 :
        return False
    if not s[:2].isalpha():
        return False
    for c in s :
        if not c.isalnum():
            return False
        if c.isdigit():
            if c == '0':
                if not found_digit :
                    condition = False
            else :
                found_digit = True
        elif found_digit and c.isalpha():
            condition = False
    return condition
main()
