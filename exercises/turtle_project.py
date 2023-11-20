"""Mountain Sunset Scene."""

from turtle import Turtle, colormode


import turtle


from random import randint


"""Above and beyond criteria: 
1. I used the circle function that was not in the tutorial to draw the sun (line 73)
2. I added a complex component by utilizing a list of colors and variables for the indices
of the list to create random colors in my sun reflection as well as alternate the mountain colors (lines 39, 52, 195)
3. I added a complex component by having three different types of sparkles present in my water and 
having the program randomize the size, orientation, location, and type of sparkle for true randomness (lines 171-187)
4. I added another complex component by creating a wave function and making it create a variety of lines in 
random lengths and locations in both hilight and lowlight colors to create depth (lines 121-132, 211-214)
Extra Note: I am completely new to programming and this took an incredibly long time but I am very proud of it :).
"""


__author__ = "730657068"


colormode(255)


al: Turtle = Turtle()


al.hideturtle()


al.speed(500)


sky_blue = (131, 160, 179)
peach = (200, 162, 151)
yellow = (254, 188, 82)
brown = (89, 76, 67)
brown_2 = (77, 65, 63)
water_blue = (2, 102, 156)
white = (255, 239, 219)
blue = (122, 198, 239)
dark_blue = (37, 69, 105)
sun_yellow = (255, 216, 126)
sun_border = (253, 221, 163)


color_list = [sky_blue, peach, yellow, brown, brown_2, brown, white, sun_yellow]


def sunset_colors() -> None:
    """Creates three color blocks to mimic a sunset sky gradient."""
    i: int = 0
    y: float = 370
    color_list_index: int = 0
    while i < 3:
        j = 0
        al.penup()
        al.goto(-370, y)
        al.pendown()
        al.color(color_list[color_list_index])
        al.begin_fill()
        al.setheading(270)
        while j < 2:
            al.forward(156)
            al.left(90)
            al.forward(740)
            al.left(90)
            j += 1
        al.end_fill()
        color_list_index += 1
        y -= 156
        i += 1


def sun() -> None:
    """Draws a circle and outlines it in a slightly lighter color to represent a sun."""
    al.penup()
    al.goto(-10, 50)
    al.pendown()
    al.color(sun_border, sun_yellow)
    al.begin_fill()
    al.circle(80)
    al.end_fill()


def mountains() -> None:
    """Draws three overlapping mountains of alternating colors and different scale sizes to create depth."""
    right_side: float = 225
    left_side = 292 * 0.5
    ground_side = 460
    x: float = -90
    k = 0
    color_list_index = 3
    while k < 3:
        al.penup()
        al.goto(x, -100)
        al.pendown()
        al.color(color_list[color_list_index])
        al.begin_fill()
        al.setheading(0)
        al.forward(ground_side)
        al.left(155)
        al.forward(right_side)
        al.left(65)
        al.forward(left_side)
        al.end_fill() 
        right_side *= 1.3
        left_side *= 1.3
        x -= 100
        color_list_index += 1 
        k += 1


def river() -> None:
    """Draws a blue block of color to create a base layer of water."""
    al.penup()
    al.goto(-370, -90)
    al.pendown()
    al.color(water_blue)
    al.begin_fill()
    al.setheading(270)
    j = 0
    while j < 2:
        al.forward(300)
        al.left(90)
        al.forward(740)
        al.left(90)
        j += 1
    al.end_fill()


def wave() -> None:
    """Draws lines of randomized length and orientation all over the block of blue to create waves."""
    p = 0
    al.setheading(180)
    while p < 50:
        m = randint(-320, 370)
        n = randint(-390, -90)
        al.penup()
        al.goto(m, n)
        al.pendown()
        al.forward(randint(10, 50))
        p += 1


def sparkle_1() -> None:
    """Draws a 5-sided star of random size to be one type of wave sparkle."""
    al.color(white)
    al.begin_fill()
    side_length = randint(2, 10)
    i = 0
    while i < 5:
        al.forward(side_length)
        al.left(144)
        i += 1
    al.end_fill()


def sparkle_2() -> None:
    """Draws a 10-sided star of random size to be another type of wave sparkle."""
    al.color(white)
    al.begin_fill()
    side_length = randint(2, 12)
    i = 0
    while i < 10:
        al.forward(side_length)
        al.left(162)
        i += 1
    al.end_fill()


def sparkle_3() -> None:
    """Draws an 8-sided star of random size to be a third type of wave sparkle."""
    al.color(white)
    al.begin_fill()
    side_length = randint(2, 15)
    i = 0
    while i < 8:
        al.forward(side_length)
        al.left(135)
        i += 1
    al.end_fill()


sparkle_list = [sparkle_1, sparkle_2, sparkle_3]


def water_sparkle() -> None:
    """Places randomly sized and randonly oriented sparkles of random type (out of the three above) in a specified domain
    among the water to be the sparkles created by the sun reflection.
    """
    al.color(white)
    r = 0
    while r < 45:
        al.setheading(randint(0, 360))
        m: int = randint(-150, 300)
        n: int = randint(-390, -100)
        sparkle_list_index = randint(0, 2)
        al.penup()
        al.goto(m, n)
        al.pendown()
        sparkle_list[sparkle_list_index]()
        r += 1


def sun_reflection() -> None:
    """Places randomly sized and randomly colored (between yellow and white) lines in a spefified domain
    among the water to be the hilighted waves created by the sun reflection.
    """
    p = 0
    al.setheading(180)
    while p < 60:
        al.color(color_list[randint(6, 7)])
        m = randint(-10, 190)
        n = randint(-390, -90)
        al.penup()
        al.goto(m, n)
        al.pendown()
        al.forward(randint(10, 50))
        p += 1


def main() -> None:
    """The entrypoint of my scene: calls all of the previously-defined 
    functions together to create a beautiful mountain sunset scene.
    """
    sunset_colors()
    sun()
    mountains()
    river()
    al.color(blue)
    wave()
    al.color(dark_blue)
    wave()
    water_sparkle()
    sun_reflection()


if __name__ == "__main__":
    main()


turtle.done()