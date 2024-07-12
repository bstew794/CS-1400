# Braeden Stewart
# CS 1400
# Assn-10

import turtle

def setup():
    turtle.screen()
    turtle.speed(75)
    turtle.setheading(90)


def drawRectanglePattern(centerX, centerY, offset, width, height, count):
    turtle.penup()
    turtle.goto(centerX, (centerY - offset))
    turtle.setheading(0)
    turtle.pendown()

    for i in range(count):
        turtle.color("red")
        turtle.circle(offset, (360 /count))

        turtle.setheading(45)
        turtle.color("Blue")
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)

    turtle.done()


drawRectanglePattern(0, 0, 25, 10, 25, 10)