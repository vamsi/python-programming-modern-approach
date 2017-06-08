from turtle import *


def draw_square(turtle):
    """
    Turtle to Draw a Square.
    """
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)


t = Turtle()
draw_square(t)
done()
