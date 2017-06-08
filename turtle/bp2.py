from turtle import *


def draw_rectangle():
    for i in range(4):
        t.forward(50)
        t.left(90)


t = Turtle()

for i in range(36):
    draw_rectangle()
    t.left(10)
done()
