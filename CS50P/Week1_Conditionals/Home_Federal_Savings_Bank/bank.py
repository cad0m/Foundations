string = input("Greeting:").lower()
if  string.split()[0] == "hello" or string.split()[0] == "hello,":
    print("$0")
elif string.split()[0][0] == "h" :
    print("$20")
else:
    print("$100")