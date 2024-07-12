# Braeden Stewart
# CS 1400
# Assn 12 - task 2

# this file defines a function that asks for a password from the user and imports the Password class /
# to check if it is a valid one

from password import Password


def main():
    repeat = True
    userInput = input("Please enter a new password: \n")
    password = Password(userInput)

    # while loop repeats until user inputs a valid password

    while repeat:
        testResult = password.isValid()

        if not testResult:
            print(password.getErrorMessage())
            userInput = input("Please enter a new password: \n")
            password.setPassword(userInput)  # sets user's new input as password variable

        else:
            print("That is a valid password, \n")
            break

    print("Thank you for your time")


main()
