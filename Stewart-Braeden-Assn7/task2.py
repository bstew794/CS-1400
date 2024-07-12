# Braeden Stewart
# CS 1400
# Assn-7: task 2

# This program determines if two circles are inside of each other, overlapping, or neither.
# These circles are given by the user.

from math import sqrt

x1, y1, r1 = eval(input("Enter dimensions of circle 1 (x, y, radius): "))
x2, y2, r2 = eval(input("Enter dimensions of circle 2 (x, y, radius): "))

distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distance < r1 - r2:
    print("circle 2 is inside of circle 1.")
elif distance < r2 - r1:
    print("circle 1 is inside of circle 2.")
elif distance < (r1 + r2):
    print("circle 2 is overlapping with circle 1.")
else:
    print("circle 2 and circle 1 do not overlap nor are inside of each other")

# End of line...