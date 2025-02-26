def main():
    x, y, z = input("Expression: ").split(" ")
    result = calculat(float(x), float(z), y)
    print(result)

def calculat(fisrt_number, second_number, operation):
    match operation:
        case "+":
            return fisrt_number + second_number
        case "-":
            return fisrt_number - second_number
        case "*":
            return fisrt_number * second_number
        case "/":
            return fisrt_number / second_number

main()
