# Braeden Stewart
#  CS 1400
#  Assn 13 - task 3

# This program draws a list of shapes according to user input

from circle import Circle
from rectangle import Rectangle
import turtle


def isColorValid(color):  # checks if user input for color is contained in list
    while color not in ["red", "green", "yellow", "blue"]:
        print("I am sorry, but you can only choose red, green, yellow, and blue.")
        color = input("Enter a color:")


def main():
    playAgain = True
    list = []

    while playAgain:
        print(" \n Enter Circle \n", "Enter Rectangle \n", "Remove Shape \n", "Draw Shapes \n", "Exit \n")

        # displays menu options and asks for user choice.

        userInput = input("What would you like to do?")

        if userInput == "Enter Circle":  # adds a circle to the object list according to user input
            centerX, centerY = eval(input("Enter the X and Y coordinates:"))
            radius = eval(input("Enter a radius:"))
            color = input("Enter a color:")

            isColorValid(color)

            circle = Circle(centerX, centerY, radius, color)
            list.append(circle)

        elif userInput == "Enter Rectangle":  # adds a rectangle to the object list according to user input
            centerX, centerY = eval(input("Enter the X and Y coordinates:"))
            height, width = eval(input("Enter a height and width:"))
            color = input("Enter a color:")

            isColorValid(color)

            rectangle = Rectangle(centerX, centerY, height, width, color)
            list.append(rectangle)

        elif userInput == "Remove Shape":  # removes an object from the object list
            print("You have", len(list), "Shapes; You can choose a number from 0 to ", (len(list) - 1), "\n")
            userInput1 = eval(input("Enter your choice:"))

            print("Are you sure you want to remove", list[userInput1], "?")
            userInput2 = input("What say you?")

            if userInput2 in ["y", "Y", "yes", "Yes"]:
                list.remove(list[userInput1])

        elif userInput == "Draw Shapes":  # draws all shapes in object list.
            turtle.clear()
            count = 0

            while count <= (len(list) - 1):
                list[count].draw()
                count += 1

        elif userInput == "Exit":  # ends the function
            break

    print("Thanks for playing!")

main()