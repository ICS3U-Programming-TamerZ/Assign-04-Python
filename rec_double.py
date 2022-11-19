#!/usr/bin/env python3

# Created By: Tamer Zreg
# Date: Nov. 18, 2022
# This program outputs the product of all numbers preceding the user's
# number using a while loop.


def main():

    # Tries to get the user's num_of_times_run, width and length as an integer.
    try:
        length = int(input("Enter a length integer that would double (cm): "))
        width = int(input("Enter a width integer that would double  (cm): "))
        num_of_times_run = int(
            input("Input the number of times you would like your program to execute: ")
        )

    # Exception thrown if the user did not enter a number for length width and times run.
    except ValueError:
        input("You must enter a positive number ranging from 1-100 Please try again.")
        return main()

    # checks if number is in range 0-100

    if (width) < 0 or (width) > 100:
        input("You must enter a number in range 0-100")
        main()
    if (length) < 0 or (length) > 100:
        input("You must enter a number in range 0-100")
        main()
    if (num_of_times_run) < 0 or (num_of_times_run) > 100:
        input("You must enter a number in range 0-100")
        main()

    # Initializing counter and product variables
    counter = 0
    product = 0

    # Code executed continually until the length and width are multiplied the times the user inputed.
    while counter < num_of_times_run:
        product = product + counter
        length = length * 2
        width = width * 2
        product = length * width
        print(f"Your Area is for {length} * {width} = {product}cm^2.")
        counter += 1


if __name__ == "__main__":
    main()
