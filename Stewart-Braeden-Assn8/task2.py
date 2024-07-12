# Braeden Stewart
# CS 1400
# Assn-8: task 2

# The purpose of this program is to simulate the monty hall problem where there are three doors on a game show.
#  Behind two of them are goats, and the last one has a car. The contestant chooses a door, and then the game show host
#  chooses a door to reveal a goat behind, and then asks the contestant if they would like to change their door.
# This program calculates the winning percentage of staying or switching.

import random
import sys

playAgain = True  # This sets the state of playAgain so we can change it later.

while playAgain is True:  # The loop repeats the program if user inputs "Y".

    userInput = input("Would you like to switch? (Y/N):")

    # the next variables ensure that the wins, counts, and percentage reset each time the outer loop begins.

    count = 0
    wins = 0
    winningPercentage = 0

    while count <= 100000:
        doors = [1, 2, 3]  # creates a list for randomly assigning values 1 - 3 to the winning door, and player door.

        winningDoor = random.choice(doors)
        playerDoor = random.choice(doors)

        # The next bit compares the values of winningDoor and playerDoor to each other
        #   to then determine the right conditions for victory.

        if playerDoor == winningDoor:

            if userInput == "N":
                wins += 1

        elif playerDoor != winningDoor:

            if userInput == "Y":
                wins += 1

        count += 1

    winningPercentage = (wins / count) * 100

    # print statement displays statistics.

    print("you have", wins, "wins, and a winning percentage of", winningPercentage)

    userInput2 = input("Would you like to play again? (Y/N):")

    # restarts while loop until user doesn't want to play.

    if userInput2 == "Y":
        playAgain = True

    else:
        sys.exit(2)
# End of line...
