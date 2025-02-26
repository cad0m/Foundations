def main():
    name = input("camelCase: ")
    snake_case(name)

def snake_case(name):
    for letter in name :
        if letter.islower():
            print(letter, sep = '', end = '')
        else:
            print('_', letter.lower(), sep = '', end = '')
    print()

main()


