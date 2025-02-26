import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):

    # check the formats
    time_result = re.search(r"(\d+)(?::(\d+))? (AM|PM) to (\d+)(?::(\d+))? (AM|PM)", s)

    if not time_result:
        raise ValueError
    else:

        # split the user input to variables can work with
        start_hour, start_minute, start_meridiem, end_hour, end_minute, end_meridiem = (
            list(time_result.groups())
        )

        # check if the user input a single number or xx:xx format
        start_minute = start_minute if start_minute is not None else "00"
        end_minute = end_minute if end_minute is not None else "00"

        # convert input to int check condition and adjust them
        start_hour = int(start_hour)
        end_hour = int(end_hour)
        start_minute = int(start_minute)
        end_minute = int(end_minute)

        # check the range of hours and minutes
        if not (0 <= start_hour <= 12 and 0 <= end_hour <= 12):
            raise ValueError
        elif not (0 <= start_minute <= 12 and 0 <= end_minute <= 12):
            raise ValueError
        else:

            # check if it pm and add +12h to make it on 24 format else if it 12 and am make it 00
            if start_meridiem == "PM" and start_hour != 12:
                start_hour += 12
            elif start_meridiem == "AM" and start_hour == 12:
                start_hour = 0

            # same thing for end hour
            if end_meridiem == "PM" and end_hour != 12:
                end_hour += 12
            elif end_meridiem == "AM" and end_hour == 12:
                end_hour = 0

            # convert the start and end to 24h format
            start = "{:02d}:{:02d}".format(start_hour, start_minute)
            end = "{:02d}:{:02d}".format(end_hour, end_minute)

            # return the final value
            return f"{start} to {end}"


if __name__ == "__main__":
    main()
