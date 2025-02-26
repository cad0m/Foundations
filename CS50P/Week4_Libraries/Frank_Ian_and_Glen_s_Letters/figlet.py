from sys import argv
from sys import exit
from pyfiglet import Figlet

figlet = Figlet()

if len(argv) == 3 and argv[1] in ["-f", "-foo"] and argv[2] in figlet.getFonts():
    figlet.setFont(font=argv[2])
    s = input("Input: ")
elif len(argv) == 1:
    s = input("Input: ")
else:
    print("Invalid usage")
    exit(1)

print("Output: " + figlet.renderText(s))
