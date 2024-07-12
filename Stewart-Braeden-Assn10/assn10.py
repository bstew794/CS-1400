# Braeden Stewart
# CS 1400
# Assn-10

# This program creates circular patterns according to user input with three options being a \
# rectangle, circle or super pattern. it also repeats if the user wishes it.

import pattern

def main():
    # Setup pattern

    pattern.setup()

    # Play again loop

    playAgain = True

    while playAgain:

        # Present a menu to the user
        # Let them select 'Super' mode or 'Single' mode\

        print("Choose a mode")
        print("1) Rectangle Pattern")
        print("2) Circle Pattern")
        print("3) Super Pattern")
        mode = eval(input("Which mode do you want to play? 1, 2 or 3: "))

        # If they choose 'Rectangle Patterns'

        if mode == 1:

            # Input Statements

            centerX, centerY = eval(input("give me some center coordinates(x,y): "))
            offset = eval(input("Give me an offset value:"))
            width = eval(input("Give me a rectangle width:"))
            height = eval(input("Give me a rectangle height:"))
            count = eval(input("How many rectangles do you want it to have?"))
            rotation = eval(input("Give me a rotation value:"))

            # Draw the rectangle pattern

            pattern.drawRectanglePattern(centerX, centerY, offset, width, height, count, rotation)

        # If they choose 'Circle Patterns'

        elif mode == 2:

            # Input Statements

            centerX, centerY = eval(input("give me some center coordinates(x,y): "))
            offset = eval(input("Give me an offset value:"))
            radius = eval(input("Give me a circle radius:"))
            count = eval(input("How many circles do you want it to have?"))

            # Draw the circle pattern

            pattern.drawCirclePattern(centerX, centerY, offset, radius, count)

        # If they choose 'Super Patterns'

        elif mode == 3:

            # Input Statements

            num = input("How many patterns do you want?")

            if num == "":
                num = 1
                pattern.drawSuperPattern(num)
            else:
                num = eval(num)
                pattern.drawSuperPattern(num)

        # Play again?

        print("Do you want to play again?")
        print("1) Yes, and keep drawings")
        print("2) Yes, and clear drawings")
        print("3) No, I am all done")
        response = eval(input("Choose 1, 2, or 3: "))

        # Statements to clear drawings and play again

        if response == 1:
            pattern.setup()
        elif response == 2:
            pattern.reset()
        elif response == 3:
            playAgain = False

    # print a message saying thank you

    print("Thanks for playing!")
    pattern.done()

main()
