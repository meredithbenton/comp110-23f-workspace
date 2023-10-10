"""Notes on Functions"""

# functions allow you to take solutions you defined in 1 place
# of your program and reuse them in other places

# Function call: expressions that return a specific type
# looks like function_name(<inputs>)

from random import randint

y: str = print("Hello!")
print(y) 
# should return "none"

x: int = round(10.25)

print(x) 

z: int = randint(1,7)
print(z)

"""Defining functions"""

# function definitions are sub-programs that define what happens when a function is called
# can be built-in, imported in Libraries, DIY- define in your python file

def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of 2 numbers"""
    if number1 >= number2: 
        return number1  
    else: #number1 < number2
        return number2

max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(other_max_number)

#example

def mimic(my_words: str) -> str: 
    """Given the string my_words, outputs the same string"""
    return my_words

mimic("Hello!")
print(mimic("Hello!"))

my_words: str = "Hello!"
response: str = mimic(my_words)
print(response)

# signature= whole top line (line 40)
# name = mimc
# parameters = my_words: str (middle of line 40)
# return type = str: (end of line 40)
# return value = my_words (line 42)

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Index too high")
    #If we made it here, that means the letter_idx is valid
    return my_words[letter_idx]
    
my_words: str = "Howdy"
letter_idx: int = len(str(my_words))