def main ():
    while True:
        try:
            fraction = input("Fraction: ")
            numbers = fraction.split('/')
            calculat = int(numbers[0]) / int(numbers[1])
        except (ValueError, ZeroDivisionError):
            pass
        else :
            if calculat <= 1:
                fuell(round(calculat, 2))
                break

def fuell(calculat):
    if calculat >= 0.99:
        print("F")
    elif calculat <= 0.01:
        print("E")
    else:
        print(f"{int(calculat*100)}%")

main ()
