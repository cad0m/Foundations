from sys import exit
import random


def main():
    level = positive_int("dkhal ra9em : ")
    number = random.randint(1, level)
    while True:
        player_input = positive_int("Guess: ", include_zero=True)
        if player_input == number:
            exit("Just right!")
        else:
            if player_input < number or player_input < 1:
                print("Too small!")
            else:
                print("Too large!")


def positive_int(promot, include_zero=False):
    while True:
        try:
            number = int(input(promot))
            if number > 0:
                return number
            elif number == 0 and include_zero:
                return number
        except ValueError:
            pass


main()
