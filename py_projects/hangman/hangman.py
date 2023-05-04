#!/usr/bin/python3

import random
from word_collection import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hang_man():
    word = get_valid_word(words)
    word_letters = set(word)
    alph = set(string.ascii_uppercase)
    used_letters = set()

    lives = 5

    while len(word_letters) > 0 and lives > 0:

        print("You have", lives, "Lives left and You have used this letter: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a Letter: ').upper()
        if user_letter in alph - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("Letter is not in the word")

        elif user_letter in used_letters:
            print('You have already used this letter.')
        else:
            print("Invalid character. Try again")

    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("You guessed the word", word, '!!!')


hang_man()
