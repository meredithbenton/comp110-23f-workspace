"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.hideturtle()
leo.speed(50)

leo.penup()
leo.goto(-150,-100)
leo.pendown()

colormode(255)
leo.color("yellow", (245, 165, 184))

leo.begin_fill()

i:int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()

bob.hideturtle()

bob.color(46, 31, 30)
bob.speed(40)

bob.penup()
bob.goto(-150,-100)
bob.pendown()

side_length: int = 300

i:int = 0
while (i < 200):
    bob.forward(side_length)
    bob.left(120)
    i += 1
    side_length *= 0.97

done()