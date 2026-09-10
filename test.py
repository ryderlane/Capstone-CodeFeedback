"""This script is to guess a random number using user input."""
import random

num_to_guess = random.randint(1, 100)
num = int(input("Guess a number"))
guessing = 1
while guessing == 1:
    if num == num_to_guess:
        print("yes!")
        guessing = 0
    elif num > num_to_guess:
        print("lower")
    elif num < num_to_guess:
        print("higher")
    else:
        print("not a valid guess")
