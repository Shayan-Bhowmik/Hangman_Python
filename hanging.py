import random
from words import words
import string

def choose_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hung_the_men():
    word = choose_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left. Used letters:", " ".join(sorted(used_letters)))
        word_display = [letter if letter in used_letters else "_" for letter in word]
        print("Current word:", " ".join(word_display))
        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print("Wrong guess!")
        elif user_input in used_letters:
            print("You already guessed that letter. Try again.")
        else:
            print("Invalid input. Enter a letter A-Z.")

    if lives == 0:
        print("\nYou died! The word was:", word)
    else:
        print("\nCongratulations! You guessed the word:", word)

hung_the_men()