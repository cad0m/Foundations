def main ():
    #ask user for answer and make it insensitive
    number = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    #check the asnwer and print resulat
    if number == "42" or number == "forty-two" or number == "forty two":
        print("Yes")
    else :
        print("No")

main()
