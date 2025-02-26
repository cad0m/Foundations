def main():
    print("Change Owed:", change())


def change():
    payed = 0
    while payed < 50 :
        while True:
            print("Amount Due:", 50 - payed)
            coins_in = int(input("Insert Coin: "))
            if coins_in in [5, 10, 25] :
                payed += coins_in
                break
    return payed - 50

main()
