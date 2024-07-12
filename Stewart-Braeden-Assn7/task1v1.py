# Braeden Stewart
# CS 1400
# Assn-7: task 1, version 1

#   This is a simple program using only conditional operators to determine
# if you win a game of Rock, Paper, Scissors against a computer.

from random import randint

userValue = eval(input("Rock (0), paper (1), scissors (2): "))
computerValue = randint(0, 2)

if computerValue == 0:
    if userValue == 0:
        print("The computer chose rock, and you also chose rock. You tied.")
    elif userValue == 1:
        print("The computer chose rock, and you chose paper. You won!")
    elif userValue == 2:
        print("The computer chose rock, and you chose scissors. You lost.")

elif computerValue == 1:
    if userValue == 0:
        print("The computer chose paper, and you chose rock. You lost.")
    elif userValue == 1:
        print("The computer chose paper, and you chose paper. You tied.")
    elif userValue == 2:
        print("The computer chose paper, and you chose scissors. You won!")

elif computerValue == 2:
    if userValue == 0:
        print("The computer chose scissors, and you chose rock. You won!")
    elif userValue == 1:
        print("The computer chose scissors, and you chose paper. You lost.")
    elif userValue == 2:
        print("The computer chose scissors, and you chose scissors as well. You tied.")

# End of line...