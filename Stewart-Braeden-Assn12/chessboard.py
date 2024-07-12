# Braeden Stewart
# CS 1400
# Assn 12 - task 1

# This file defines the chessboard class which is then used to draw a chessboard according to its variables

import turtle


class Chessboard:
    def __init__(self, startX, startY, width=250, height=250):
        self.___startX = startX
        self.__startY = startY
        self.__width = width
        self.__height = height

    def __drawBorder(self):
        turtle.penup()
        turtle.goto(self.___startX, self.__startY)
        turtle.pendown()
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)

    def __drawRectangle(self, centerX):
        sideLengthX = self.__width / 8
        sideLengthY = self.__height / 8

        turtle.penup()
        turtle.goto(centerX, self.__startY)
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(sideLengthX)
        turtle.left(90)
        turtle.forward(sideLengthY)
        turtle.left(90)
        turtle.forward(sideLengthX)
        turtle.left(90)
        turtle.forward(sideLengthY)
        turtle.end_fill()
        turtle.left(90)

    def __drawAllRectangles(self):
        stepY = 1

        while stepY <= 8:
            stepX = 1
            centerX = 0

            while stepX <= 8:
                if (stepX + stepY) % 2 == 0:
                    self.__drawRectangle(centerX)

                stepX += 1
                centerX += (self.__width / 8)

            stepY += 1
            self.__startY += (self.__height / 8)

    def draw(self):
        self.__drawBorder()
        self.__drawAllRectangles()