def main():
    #ask user for the mass
    mass = int(input("m: "))
    #printing the result
    print("E:", fromul(mass))

def fromul(mass):
    #calculing the energie
    return mass * 300000000 * 300000000

main()

