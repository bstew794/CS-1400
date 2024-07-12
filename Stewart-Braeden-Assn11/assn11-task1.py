# Braeden Stewart
# CS 1400
# Assn 11 - task 1

# This program draws a face using turtle and then asks the user for input to change the state of the face.

import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True



    def __draw_head(self):
        if self.is_happy():
            turtle.color("Yellow")
        elif not self.is_happy():
            turtle.color("Red")

        turtle.width(1)
        turtle.speed(2)

        turtle.setheading(0)
        turtle.penup()
        turtle.goto(0, -100)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()


    def __draw_eyes(self):
        if self.is_dark_eyes():
            turtle.color("Black")
        elif not self.is_dark_eyes():
            turtle.color("Blue")

        turtle.setheading(0)
        turtle.penup()
        turtle.goto(-25, 40)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(10)
        turtle.end_fill()


    def __draw_mouth(self):
        turtle.color("Black")

        if self.is_smile():
            turtle.setheading(270)
            turtle.width(3)
            turtle.penup()
            turtle.goto(-50, 0)
            turtle.pendown()
            turtle.circle(50, 180)

        elif not self.is_smile():
            turtle.setheading(90)
            turtle.width(3)
            turtle.penup()
            turtle.goto(50, -50)
            turtle.pendown()
            turtle.circle(50, 180)


    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()


    def is_smile(self):
        if self.__smile:
            return True
        else:
            return False

    def is_happy(self):
        if self.__happy:
            return True
        else:
            return False
    def is_dark_eyes(self):
        if self.__dark_eyes:
            return True
        else:
            return False

    def change_mouth(self):
        if self.is_smile():
            self.__smile = False
        elif not self.is_smile():
            self.__smile = True

        self.draw_face()

    def change_emotion(self):
        if self.is_happy():
            self.__happy = False
        elif not self.is_happy():
            self.__happy = True

        self.draw_face()

    def change_eyes(self):
        if self.is_dark_eyes():
            self.__dark_eyes = False
        elif not self.is_dark_eyes():
            self.__dark_eyes = True

        self.draw_face()


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else "happy"
        eyes = "blue" if face.is_dark_eyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()
