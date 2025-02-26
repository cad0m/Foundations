def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            date = input("Date :").title()
            if "/" in date :
                month, day, year = date.split("/")
            if "," in date :
                date, year = date.split(",")
                month, day = date.split(" ")
                month = months.index(month) + 1
            if (0 <= int(year) <= 2025) and (1 <= int(month) <= 12) and (1<= int(day) <= 31):
                print(f"{int(year)}-{int(month):02}-{int(day):02}", end = '')
                break
        except (ValueError, UnboundLocalError):
            pass


main()


