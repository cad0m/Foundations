def main():
    time = input("What time is it? ")

    match convert(time) :
        case n if 7 <= n <= 8 :
            print("breakfast time")
        case n if 12 <= n <= 13 :
            print("lunch time")
        case n if 18 <= n <= 19 :
            print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    converted = float(hours) + (float(minutes)/60)
    return converted

if __name__ == "__main__":
    main()
