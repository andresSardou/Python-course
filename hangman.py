# # # Step 1
import random
from hangman_words import word_list
from hangman_art import logo
from hangman_art import stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
guesses = []
for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already typed the letter: {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        guesses += guess
        lives -= 1
        print(stages[lives + 1])
        print(f"{guess.upper()} is not in the word.\nYou have {lives} lives remaining.\n"
              f"You have guessed the following letters: {' '.join(guesses)}")
        if lives == 0:
            print(stages[lives])
            print("You lose")
            break

if "_" not in display:
    print("You win")

