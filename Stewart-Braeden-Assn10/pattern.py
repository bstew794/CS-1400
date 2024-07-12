# Braeden Stewart
# CS 1400
# Assn-10

# This python file contains all the functions necessary to run assn10.py

import turtle
import random


def done():
    turtle.done()

# inserts settings for turtle to start with

def setup():
    turtle.setup(1000, 800)
    turtle.speed(25)
    turtle.width(2)
    turtle.setheading(90)

# rests the turtle screen

def reset():
    turtle.clear()

def setRandomColor():
    colors = ["red", "green", "black", "blue", "purple", "olive"]
    color = random.choice(colors)
    turtle.color(color)


def drawRectangle(width, height, rotation):
    turtle.right(rotation)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90 - rotation)


def drawCircle(radius):
    turtle.right(180)
    turtle.circle(radius)
    turtle.right(180)


def drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation):
    turtle.penup()
    turtle.setheading(90)
    turtle.goto((centerX + (offset / 2)), centerY)  # sends turtle to center-point

    for i in range(count):

        # draws a circle segment first then rectangles repeatably afterwards until pattern is finished

        turtle.penup()
        turtle.color("white")
        turtle.circle((offset / 2), (360 / count))
        turtle.pendown()
        setRandomColor()

        drawRectangle(width, height, rotation)


def drawCirclePattern(centerX, centerY, offset, radius, count):
    turtle.penup()
    turtle.setheading(90)
    turtle.goto((centerX + (offset / 2)), centerY)

    for i in range(count):

        # draws a circle segment first then circles repeatably afterwards until pattern is finished

        turtle.pendown()
        turtle.penup()
        turtle.color("white")
        turtle.circle((offset / 2), (360 / count))
        turtle.pendown()

        setRandomColor()
        drawCircle(radius)

def drawSuperPattern(num):
    for i in range(num):  # repeats pattern generation according to input variable: num

        # random assignment of values to variables:

        centerX = random.randint(-500, 501)
        centerY = random.randint(-400, 401)
        offset = random.randint(-200, 201)
        count = random.randint(1, 101)
        patternChoices= [1, 2]
        choice = random.choice(patternChoices)  # chooses between a circle pattern or rectangle pattern

        if choice == 1:
            width = random.randint(1, 101)
            height = random.randint(1, 101)
            rotation = random.randint(-360, 361)

            drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        elif choice == 2:
            radius = random.randint(1, 51)

            drawCirclePattern(centerX, centerY, offset, radius, count)