# TASK 1: Hangman Game
# 🖥 Python Programming — Internship Overview

# Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
# Simplified Scope:
# ● Use a small list of 5 predefined words (no need to use a file or API).
# ● Limit incorrect guesses to 6.
# ● Basic console input/output — no graphics or audio.
# Key Concepts Used: random, while loop, if-else, strings, lists.




import random
# built in python module used to generate random values

# predefined words list(5 words)
words = ["ram", "shyam", "hari", "sita", "rita"]

# random words
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("\nWelcome to Hangman! ")
print("You have 6 incorrect guesses allowed.")
print("_"*50)
# game while loop

while incorrect_guesses < max_guesses:
    display_word = ""

    #build display setting
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter 
        else:
            display_word += "_"

            
    print("Word:", display_word)
    print("Remaining guesses left:", max_guesses - incorrect_guesses)
    print("Guessed letters:", ", ".join(guessed_letters))
    print("-"*50)

    # Check win condition
    if "_" not in display_word:
        print("Congratulations you win! The word was:", secret_word)
        print("-"*50)
        break

    guess = input("Enter a letter: ").strip().lower()

    # Validate input
    if len(guess) != 1:
        print("Invalid input. Enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("Already guessed. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        incorrect_guesses += 1
        print("Wrong guess!")
    else:
        print("Correct!")
    

# Lose condition
if incorrect_guesses == max_guesses:   
    print("Guessed letters:", ", ".join(guessed_letters))
    print("-"*50)
    print("Sorry game over! The word was:", secret_word)
    print("-"*50)