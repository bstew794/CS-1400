# Braeden Stewart
# CS 1400
# Assn-9

# This file contains all the functions to be used when drawing a chessboard.

import turtle

# the function drawRectangle draws a rectangle using the turtle module with the given variables.

def drawRectangle (height = 30, width = 30, xOrigin = 0, yOrigin = 0, color = "black"):
    turtle.penup()
    turtle.goto(xOrigin + (width / 2), yOrigin + (height / 2))
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.end_fill()

# drawAllRectangles creates the checker pattern of the board by repeatably using drawRectangle,
# only drawing a black rectangle at certain points on the chessboard.
# I chose the positions where the sum of stepX, and stepY was an even number.
# The larger while loop serves to shift the rectangles vertically,
# and the nested one serves to shift the rectangles horizontally.

def drawAllRectangles (height, width, xOrigin, yOrigin):
    sideLengthX = width / 8
    sideLengthY = height / 8
    centerY = (yOrigin - (height / 2)) + sideLengthY / 2
    stepY = 1

    while stepY <= 8:
        stepX = 1
        centerX = (xOrigin - (width / 2)) + sideLengthX / 2

        while stepX <= 8:
            if (stepX + stepY) % 2 == 0:
                drawRectangle(sideLengthY, sideLengthX, centerX, centerY)

            centerX += sideLengthX
            stepX += 1

        stepY += 1
        centerY += sideLengthY

    turtle.done()

# drawChessboard displays the chessboard in its entirety with border included.

def drawChessboard (startX, startY, width, height):
    rectangleX = startX + width / 2
    rectangleY = startY + height / 2

    turtle.penup()
    turtle.goto(rectangleX, rectangleY)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)

    drawAllRectangles(height, width, startX, startY)

# main() determines whether to use the default value of 250 for width and height or not based upon what is given.

def main (startX = 0, startY = 0, width = 250, height = 250):

    if width == "" and height == "":
        drawChessboard(int(startX), int(startY), width=250, height=250)

    elif height == "":
        drawChessboard(int(startX), int(startY), int(width), height=250)

    elif width == "":
        height = int(height)
        width = 250
        drawChessboard(int(startX), int(startY), width, height)

    else:
        drawChessboard(int(startX), int(startY), int(width), int(height))

# end of line...
