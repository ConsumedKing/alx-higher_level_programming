#!/usr/bin/python3
def print_last_digit(number):
    # Calculate the absolute value of the number to handle negative
    number = abs(number)
    # Get the last digit by taking the remainder when divided by 10.
    last_digit = number % 10
    # Print the last digit.
    print(last_digit, end="")
    # Return the value of the last digit.
    return last_digit
