
"""EX03 - Structured Wordle."""


__author__ = "730657068"


def contains_char(secret_word: str, char_search: str) -> bool:
    """Searches whether a character matches any character in the answer."""
    secret_word_index: int = 0
    assert len(char_search) == 1
    while secret_word_index < len(secret_word):
        if char_search == secret_word[secret_word_index]:
            return True
        else: 
            secret_word_index += 1
    return False


def emojified(guess: str, secret_word: str) -> str:
    """Makes a string of colored boxes to show the word comparison."""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    colors: str = ""
    guess_index: int = 0
    while guess_index < len(secret_word):
        if guess[guess_index] == secret_word[guess_index]:
            colors = (f"{colors}{GREEN_BOX}")
        elif contains_char(secret_word, guess[guess_index]):
            colors = (f"{colors}{YELLOW_BOX}")
        else:
            colors = (f"{colors}{WHITE_BOX}")
        guess_index += 1
    return colors


def input_guess(expected_length: int) -> str:
    """Checks that the guess input is the same as the length of secret word."""
    word: str = input(f"Enter a {expected_length} character word: ")
    while len(word) != expected_length:
        word_retry: str = input(f"That wasn't {expected_length} chars! Try again: ")
        word = word_retry
    return (word)
    

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    secret_word: str = "codes"
    winning_loop = False
    while turn_number <= 6 and winning_loop is False:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret_word))
        result = emojified(guess, secret_word)
        if guess == secret_word:
            print(result)
            print(f"You won in {turn_number}/6 turns!")
            winning_loop = True
            return
        else:
            print(result)
            turn_number += 1
    if turn_number > 6:
        print("X/6 - Sorry, try again tomorrow!")
        return
    

if __name__ == "__main__":
    main()