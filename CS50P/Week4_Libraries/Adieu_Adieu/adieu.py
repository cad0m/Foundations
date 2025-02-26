def main():
    names = []
    while True:
        try:
            promot = input("Name: ").title().strip()
            names.append(promot)
        except EOFError:
            print()
            break

    count = len(names)
    print("Adieu, adieu, to", end = '')
    for name in names:
        print(f" {name}", end = '')
        if (count >= 2):
            if (len(names) != 2):
                print(",", end = '')
            if count == 2 :
                print(" and", end = '')
        count -= 1
    print()
main ()
