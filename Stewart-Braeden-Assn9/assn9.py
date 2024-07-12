# Braeden Stewart
# CS 1400
# Assn-9

# This program draws a chessboard when given an input by the user for location, width, and height.
# Refer to chessboard.py in the same folder for further information regarding the process.

import chessboard

xOrigin = input("Please give me an x-component:")
yOrigin = input("Please give me an y-component:")
width = input("Please give me the desired width:")
height = input("Please give me the desire height:")

chessboard.main(xOrigin, yOrigin, width, height)