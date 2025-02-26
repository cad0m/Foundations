from validator_collection import is_email


def main():
    print(is_valid(input("What's your email address? ")))


def is_valid(s):
    if is_email(s):
        return "valid"
    return "Invalid"


if __name__ == "__main__":
    main()
