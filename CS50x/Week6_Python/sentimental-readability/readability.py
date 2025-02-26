from cs50 import get_string


def main():
    text = get_string("text : ")
    Wa = count_words(text)
    La = count_letters(text) / Wa * 100
    Sa = count_sentences(text) / Wa * 100
    index = 0.0588 * La - 0.296 * Sa - 15.8

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        note = str(round(index))
        print(f"Grade {note}")


def count_letters(text):
    count = 0
    for i in range(len(text)):
        if text[i].isalpha():
            count += 1
    return count


def count_words(text):
    count = 1
    for i in range(len(text)):
        if text[i].isspace():
            count += 1
    return count


def count_sentences(text):
    count = 0
    for i in range(len(text)):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            count += 1
    return count


main()
