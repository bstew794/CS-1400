# Braeden Stewart
#  CS 1400
#  Assn 13 - task 3

# This file contains the information and methods for the Circle class

import turtle


class Circle:
    def __init__(self, centerX, centerY, radius, color):
        self.__centerX, self.__centerY = centerX, centerY
        self.__radius = radius
        self.__color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.__centerX, (self.__centerY - self.__radius))
        turtle.pendown()
        turtle.color(self.__color)
        turtle.begin_fill()
        turtle.circle(self.__radius)
        turtle.end_fill()

