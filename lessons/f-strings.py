"""Unicode, Emoji, Escape Sequences, and f-strings"""

#f-strings can be used to make printing integers easier!
course: int = 110
print("I am in COMP" + str(course) + " right now!")
      
print(f"I am in COMP{ course } right now!")

name: str = "Lauren"
age_turning : int = 21
print("Hello " + name + ", you're almost " + str(age_turning) + "!")
print (f"Hello {name}, you're almost {age_turning}!")
#normal number system is base-10 (ex. 90)
#binary is base-2
#Hexadecimal is base 16 and has 16 digits 0-9 followed by A-F
#A-F corresponds to decimal values 10-15
#python has a built-in hex function for converting to its representation
print(hex(90))

#emojis
emoji: str = "\U0001F920\U0001F40E"
print(emoji)
print(len(emoji))
print(emoji[0])

print(chr(129313))
print("110 is on a \U0001F6A2")

#escape sequences signal that something special is about to follow the backlash
#refer to notes for specifics, below are some examples
print("Hello\nworld\n!!!")
print("The computer said, \"Hello, world.\"")
print("\tHello, world")
print("\\Hello, world\\")

#ord is short for "ordinal" which is the order in which characters
#are defined, takes a single-character string as an input parameter
#and returns the int representation of the character's binary code
print(ord("A"))
print(ord("B"))
print(ord("a"))
print(ord("b"))
#use the chr function to convert an int to a character
print(chr(65))
print(chr(122))
print(chr(ord('A')))
print(ord(chr(65)))
