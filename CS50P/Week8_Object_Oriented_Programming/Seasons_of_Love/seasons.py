import inflect
import sys
from datetime import date


def main():
    print(age_in_words(input("Date of Birth: ")))



def age_in_words(birth_date):
    try:
        p = inflect.engine()
        birth_date = date.fromisoformat(birth_date)
        date_difference = date.__sub__(date.today(), birth_date)
        return p.number_to_words(date_difference.days * 24 * 60).capitalize().replace(" and", "") + " minutes"
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
