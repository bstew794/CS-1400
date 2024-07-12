# Braeden Stewart
# CS 1400
# Assn-6: Task 1

# This program makes polygon calculations easy.
#  with just the number of sides and the side length, the user is given the area of the polygon
#  *only works with regular polygons (equal side lengths, and interior angles)*

from math import pow
from math import tan
from math import pi

numberOfSides = abs(eval(input("Enter the number of sides: ")))
sideLength = eval(input("Enter the length of one side: "))

area = round((numberOfSides * pow(sideLength, 2)) / (4 * tan(pi / numberOfSides)), 5)

print("The area of the polygon is", area)

# end of line...