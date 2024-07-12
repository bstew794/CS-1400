# Braeden Stewart
# CS 1400
# Assn-4: Task 1

# this file creates a happy soviet snowman greeting you while Russia's flag watches on from the background.
# It is recommended you play the USSR anthem while the turtle is drawing for full cheeky breeki!

import turtle

# background (Russian Flag):

turtle.penup()
turtle.width(2)
turtle.speed(4)

turtle.goto(-300,300)
turtle.color("black")
turtle.pendown()
turtle.forward(600)
turtle.right(90)
turtle.forward(100)

turtle.color("medium blue")
turtle.right(90)
turtle.begin_fill()
turtle.forward(600)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()

turtle.penup()
turtle.color("red")

turtle.goto(300,100)
turtle.setheading(270)
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.penup()
turtle.goto(-300,300)
turtle.right(180)
turtle.pendown()
turtle.color("black")
turtle.forward(100)

# Body:
turtle.penup()
turtle.setheading(0)
turtle.width(4)
turtle.speed(4)
turtle.goto(0,0)

turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("white")
turtle.pencolor("black")
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(35)
turtle.end_fill()

turtle.penup()
turtle.goto(0,170)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

# Left Arm:

turtle.penup()
turtle.width(5)
turtle.goto(35,135)

turtle.pendown()
turtle.goto(85,50)
turtle.penup()
turtle.goto(75,70)
turtle.pendown()
turtle.goto(95,70)
turtle.penup()
turtle.goto(75,70)
turtle.pendown()
turtle.goto(75,50)

# Right Arm:

turtle.penup()
turtle.width(5)
turtle.goto(-35,135)

turtle.pendown()
turtle.goto(-65,125)
turtle.goto(-105,165)
turtle.penup()
turtle.goto(-85,145)
turtle.pendown()
turtle.goto(-90,175)
turtle.penup()
turtle.goto(-85,145)
turtle.pendown()
turtle.goto(-105,145)

# Hat:

turtle.penup()
turtle.width(3)
turtle.color("oliveDrab4")
turtle.goto(0,207.5)
turtle.pendown()
turtle.begin_fill()
turtle.forward(40)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(40)
turtle.end_fill()

# Hat Band:

turtle.penup()
turtle.width(2)
turtle.color("saddle brown")
turtle.goto(20,212.5)
turtle.pendown()
turtle.begin_fill()
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(40)
turtle.end_fill()

# Soviet star:
# learned how to do star from comment on StackOverflow.com
# here is link: https://stackoverflow.com/questions/26356543/turtle-graphics-draw-a-star

turtle.penup()
turtle.width(1)
turtle.goto(0,235)
turtle.setheading(90)
turtle.pendown()

STAR_SIZE = 20

EXPANSION = 1.2
TRANSLATION = STAR_SIZE * EXPANSION / 4

turtle.hideturtle()
turtle.color("dark red")
turtle.shape("triangle")
turtle.turtlesize(STAR_SIZE * EXPANSION / 20)

for _ in range(5):
    turtle.right(72)
    turtle.forward(TRANSLATION)
    turtle.stamp()
    turtle.backward(TRANSLATION)

# Coat Buttons:

turtle.penup()
turtle.width(3)
turtle.color("goldenrod")
turtle.goto(0,110)
turtle.right(90)

turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.goto(0,125)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.goto(0,140)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

# Eyes, and Mouth:

turtle.penup()
turtle.goto(-10,185)
turtle.right(90)
turtle.color("black")
turtle.pendown()
turtle.begin_fill()
turtle.circle(10,180)
turtle.left(90)
turtle.forward(20)
turtle.fillcolor("dark red")
turtle.end_fill()

turtle.penup()
turtle.goto(-15,190)
turtle.left(180)
turtle.pendown()
turtle.circle(5,180)

turtle.penup()
turtle.goto(15,200)
turtle.pendown()
turtle.circle(5,180)

turtle.done()