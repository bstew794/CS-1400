# Braeden Stewart
#  CS 1400
#  Assn 13 - task 3

# This file contains the information and methods for the Rectangle class

import turtle


class Rectangle:
    def __init__(self, centerX, centerY, height, width, color):
        self.__centerX, self.__centerY = centerX, centerY
        self.__height, self.__width = height, width
        self.__color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.__centerX, self.__centerY)
        turtle.pendown()
        turtle.color(self.__color)
        turtle.begin_fill()
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.end_fill()

