# Braeden Stewart
# CS 1400
# Assn-7: task 1, version 1

#   This is a simple program using only conditional operators to determine
# if you win a game of Rock, Paper, Scissors against a computer.

from random import randint
import sys

userValue = eval(input("Rock (0), paper (1), scissors (2): "))
computerValue = randint(0, 2)

if not (userValue == 0 or userValue == 1 or userValue == 2):
    print("Unacceptable!!!")
    sys.exit(2)
else:
    if computerValue == 0 and userValue == 0:
        print("The computer chose rock, and so did you. You tied.")
    elif computerValue == 0 and userValue == 1:
        print("The Computer chose rock, and you chose paper. You won!")
    elif computerValue == 0 and userValue == 2:
        print("The Computer chose rock, and you chose scissors. You lost.")

    elif computerValue == 1 and userValue == 0:
        print("The Computer chose paper, and you chose rock. You lost.")
    elif computerValue == 1 and userValue == 1:
        print("The Computer chose paper, and so did you. You tied.")
    elif computerValue == 1 and userValue == 2:
        print("The Computer chose paper, and you chose scissors. You won!")

    elif computerValue == 2 and userValue == 0:
        print("The Computer chose scissors, and you chose rock. You won!")
    elif computerValue == 2 and userValue == 1:
        print("The Computer chose scissors, and you chose paper. You lost.")
    elif computerValue == 2 and userValue == 2:
        print("The Computer chose scissors, and so did you. You tied.")

# End of line...