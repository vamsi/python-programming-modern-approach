from turtle import *
import random


def random_walk(turtle, turns, distance=20):
    """
     Turns a random number of degrees and moves
     a given distance for a fixed number of turns.
    """
    turtle.width(1)
    for x in range(turns):
        turtle.rt(random.randint(0, 360))
        turtle.forward(distance)


random_walk(Turtle(), 30)
done()
