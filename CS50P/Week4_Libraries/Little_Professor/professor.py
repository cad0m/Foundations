import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        count = 0
        first_number = generate_integer(level)
        second_number = generate_integer(level)
        summ = first_number + second_number
        while count < 3:
            try:
                if summ == int(input(f"{first_number} + {second_number} = ")):
                    score += 1
                    break
            except ValueError:
                print("EEE")
                count += 1
            else:
                print("EEE")
                count += 1

        if count == 3:
            print(f"{first_number} + {second_number} = {summ}")
    print("score: ", score)


def get_level():
    while True:
        try:
            number = int(input("Level: "))
            if number not in [1, 2, 3]:
                raise ValueError
            else:
                return number
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
