def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # removing dollar sign
    d = d.removeprefix("$")
    #retrun amount as float
    return float(d)



def percent_to_float(p):
    # removing porcentage sign
    p = p.removesuffix("%")
    #make it float and in decimal form
    p = float(p) / 100
    #returning amount
    return p

main()
