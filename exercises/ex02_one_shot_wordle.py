
"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730657068"

secret_word = str("python")
word_guess = str(input(f"What is your {len(str(secret_word))}-letter guess? "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
colors = str("")

secret_word_index: int = 0
word_guess_index: int = 0
letter_match = False

while len(str(word_guess)) != len(secret_word):
    # while the inputted word is the wrong length
    wordle_word_reattempt: str = input(f"That was not {len(secret_word)} letters! Try again: ")
    # give the player a chance to reattempt
    word_guess = wordle_word_reattempt

if len(word_guess) == len(secret_word):
    # if the word is the correct length
    while secret_word_index < len(secret_word):
        # while the letter that the program is checking is up to the last letter of the secret word
        if str(secret_word[secret_word_index]) == str(word_guess[secret_word_index]):
            # if the correct letter was guessed, add a green box to the string of colors and move on to the next letter
            colors = (f"{colors}{GREEN_BOX}")
            secret_word_index = secret_word_index + 1
        else: 
            word_guess_index = 0
            letter_match = False
            while letter_match is False and word_guess_index < len(secret_word):
                if str(secret_word[word_guess_index]) == str(word_guess[secret_word_index]):
                    colors = (f"{colors}{YELLOW_BOX}")
                    secret_word_index = secret_word_index + 1
                    letter_match = True
                else:
                    word_guess_index = word_guess_index + 1 
                if word_guess_index == len(secret_word):
                    colors = (f"{colors}{WHITE_BOX}")
                    secret_word_index = secret_word_index + 1
                    letter_match = True


print(colors)

if str(word_guess) == str(secret_word):
    print("Woo! You got it!")
elif len(str(word_guess)) == len(str(secret_word)) and str(word_guess) != str(secret_word):
    print("Not quite. Play again soon!")



    



    
