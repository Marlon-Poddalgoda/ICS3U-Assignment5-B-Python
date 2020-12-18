#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program calculates the times table of a user input

import constants


def main():
    # this function will calculate the times table of a user input

    print("This program displays the multiplication table of a user input.")
    print("")

    # loop counter variable
    loop_counter = 0

    # sum of positive integers variable
    answer = 0

    # input
    user_input = input("Enter a positive integer: ")
    print("")

    # process
    try:
        user_input_int = int(user_input)

        if user_input_int > 0:
            # loop statement
            while loop_counter <= constants.MAX_MULTIPLICATION:
                # calculations
                answer = user_input_int * loop_counter
                print("{0} x {1} = {2}".format(user_input_int, loop_counter,
                                               answer))
                loop_counter = loop_counter + 1
        else:
            # output
            print("{} is not a positive integer!"
                  .format(user_input_int))
    except Exception:
        # output
        print("That's not a number! Try again.")
    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
