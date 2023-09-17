"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730657068"              

wordle_word: str = input("Enter a 5-character word: ")

if len(str(wordle_word)) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character_input: str = input("Enter a single character: ")

if len(str(character_input)) != 1:
    print("Error: Character must be a single character.")
    exit()

number_of_instances: int = 0

print("Searching for " + character_input + " in " + wordle_word)

if character_input == str(wordle_word)[0]:
    number_of_instances = number_of_instances + 1
    print(character_input + " found at index 0" )

if character_input == str(wordle_word)[1]:
    print(character_input + " found at index 1" )
    number_of_instances = number_of_instances + 1

if character_input == str(wordle_word)[2]:
    print(character_input + " found at index 2" )
    number_of_instances = number_of_instances + 1

if character_input == str(wordle_word)[3]:
    print(character_input + " found at index 3" )
    number_of_instances = number_of_instances + 1

if character_input == str(wordle_word)[4]:
    print(character_input + " found at index 4" )
    number_of_instances = number_of_instances + 1


if number_of_instances == 0:
    print("No instances of " + character_input + " found in " + wordle_word)
if number_of_instances == 1:
    print(str(number_of_instances) + " instance of " + str(character_input) + " found in " + str(wordle_word))
if number_of_instances > 1:
    print(str(number_of_instances) + " instances of " + str(character_input) + " found in " + str(wordle_word))