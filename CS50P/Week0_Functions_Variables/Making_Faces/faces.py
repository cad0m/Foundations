def main():
    emoticon = input()
    print(convert(emoticon))

def convert(emoticon):
    emoticon = emoticon.replace(":)", "\U0001F642")
    emoticon = emoticon.replace(":(", "\U0001F641")
    return emoticon

main()



