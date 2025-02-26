def main():
    text = input("Input: ")
    print('Output: ',)
    shorten(text)

def shorten(word):
    for letter in word:
        if letter.upper() not in ['A', 'E', 'I', 'O', 'U']:
            print(letter, sep = '', end = '')
    print()


if __name__ == "__main__":
    main()
