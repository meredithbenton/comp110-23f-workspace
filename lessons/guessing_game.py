"""Program taht loops until correct number is guessed"""

from random import randint

secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
#note that the input needs to be assigned as a integer bc it automatically goes to a string

while guess != secret:
    print("Wrong!")
    guess = int(input("Guess again: "))
#variable needs to be reassigned so that the loop is not indefinite
print("You guessed correctly!")
