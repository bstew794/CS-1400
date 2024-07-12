# Braeden Stewart
# CS 1400
# Assn-5: Task 2

# This program takes you into the amazing world of imagination by taking the role of an anonymous soviet archer.
# You are then guided to pick the target size and location by Boris, who then questions reality later on.

print("")
print("Anon....")
print("Are you awake?")
print("Wake up, our instructor awaits us at the archery range!")
print("[you make your way to the range]")
print("")

print("Anon, where do you want the target to be centered at?")
print("")

xOrigin = eval(input("Enter a X Value:"))
print("")
yComponent = eval(input("Enter a Y value:"))
print("")

print("Okay, now how large do you want the bullseye to be?")
print("")

bullseyeRadius = eval(input("Enter a radius:"))
print("")

print("Alright, constructing target now...")
print("")

import turtle

# Target construction:

turtle.penup()
turtle.speed(3)
turtle.width(3)
turtle.hideturtle()

# This is the target construction phase:

yOrigin = yComponent - 75
radius = bullseyeRadius + 75

turtle.goto(xOrigin, yOrigin)
turtle.begin_fill()
turtle.pendown()
turtle.circle(radius)
turtle.end_fill()

radius -= 25
yOrigin += 25

turtle.penup()
turtle.goto(xOrigin, yOrigin)
turtle.color("purple")
turtle.begin_fill()
turtle.pendown()
turtle.circle(radius)
turtle.end_fill()

radius -= 25
yOrigin += 25

turtle.penup()
turtle.goto(xOrigin, yOrigin)
turtle.color("green")
turtle.begin_fill()
turtle.pendown()
turtle.circle(radius)
turtle.end_fill()

radius -= 25
yOrigin += 25

turtle.penup()
turtle.goto(xOrigin, yOrigin)
turtle.begin_fill()
turtle.color("yellow")
turtle.pendown()
turtle.circle(bullseyeRadius)
turtle.end_fill()

turtle.done()

# The rest of this is fun, but pointless roleplay with an IF and ELSE statment.

print("")
print("What?! You saw green and purple on the target?!")
print("...")
vodka = input("Are you sure you didn't drink too much Vodka last night, my comrade?")

if vodka in ["y", "Y", "Yes", "yes", "YES"]:
    print("[Boris smacks you upside the head.]")
    print("No more Vodka for you!")

else:
    print("")
    print("Then maybe this is all a dream...")
    print("")
    print("[Boris spins a top on the nearby bench, but it eerily continues to spin.]")
    print("...")
    print("")
    print("Or it's just a missing texture within this program, so get out of here!")
    print("")
    print("[The top teeters]")

# The End!