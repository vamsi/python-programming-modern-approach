from turtle import *
turtle = Turtle()

turtle.color("blue")

for i in range(50):
    turtle.forward(50)
    turtle.left(123)  # Let's go counterclockwise this time

turtle.color("red")
for i in range(50):
    turtle.forward(100)
    turtle.left(123)

done()
