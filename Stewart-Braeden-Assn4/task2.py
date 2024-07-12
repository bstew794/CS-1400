# Braeden Stewart
# CS 1400
# Assn-4: Task 2

# This program evaluates the user's input to find the surface area and volume of a cuboid.

print("Welcome to the Cuboid Calculator! ")
print("Please enter values in feet.")

length = eval(input("Enter the length:"))
width = eval(input("Enter the width:"))
height = eval(input("Enter the width:"))

print("Your", length, "X", width, "X", height, "cuboid has a volume of", length * width * height,
      "cubic feet and a surface area of",
      (2 * length * width) + (2 * length * height) + (2 * height * width), "square feet.")
