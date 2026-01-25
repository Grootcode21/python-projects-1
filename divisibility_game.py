import random
import sys

def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")

def check_divisibility(number, divisor):
    return number % divisor == 0