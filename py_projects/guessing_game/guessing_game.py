#!/usr/bin/python3
"""
    A Simple Number guessing game
"""

import random
import time


game_mode = input("Select Game Mode: User or COM: ")

print("x------------------------------------------------------------------------x")
min_range = int(input('Enter the minimum range of guess: '))
max_range = int(input('Enter the maximum range of guess: '))

print("x------------------------------------------------------------------------x")


def my_guessing_game():

    def user_guess_game():
        random_num = random.randint(min_range, max_range)
        while True:
            guess = int(input("Guess the Number: "))
            if guess < random_num:
                print("Guess again. Too low")
            elif guess > random_num:
                print("Guess again. Too high")
            else:
                print("x-----------------------------------------------------------x")
                print("Congrats. You have guessed {} correctly".format(random_num))
                print("x-----------------------------------------------------------x")

                proceed = input("Do you want to play again (Yes) or (No): ")
                if proceed.lower() == "yes":
                    user_guess_game()
                elif proceed.lower() == "no":
                    exit()

    def com_guess_game():
        my_num = int(input("Pick a Number: "))
        while True:
            com_guess = random.randint(min_range, max_range)
            if com_guess < my_num:
                print("Computer guessed {} and its too low".format(com_guess))
                time.sleep(0.5)
            elif com_guess > my_num:
                print("Computer guessed {} and its too high".format(com_guess))
                time.sleep(0.5)
            else:
                print("x-----------------------------------------------------------x")
                print("Computer guessed {} and it is correct".format(com_guess))
                print("x-----------------------------------------------------------x")

                proceed = input("Do you want to play again (Yes) or (No): ")
                if proceed.lower() == "yes":
                    com_guess_game()
                elif proceed.lower() == "no":
                    exit()

    if game_mode.upper() == "USER":
        user_guess_game()
    elif game_mode.upper() == "COM":
        com_guess_game()


my_guessing_game()
