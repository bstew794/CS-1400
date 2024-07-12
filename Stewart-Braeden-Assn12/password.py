# Braeden Stewart
# CS 1400
# Assn 12 - task 2

# This file contains the Password class that defines methods to check if a password meets certain conditions
# additionally, it returns a error message if the password is not valid.


class Password:
    def __init__(self, password):
        self.__password = password
        self.__message = ""

    def setPassword(self, password):
        self.__password = password

    def getErrorMessage(self):
        return self.__message

    def isValid(self):
        s = self.__password   # s stands for string
        result = s.find("password")

        if result != -1:  # if "password" is found in the password then it prints an error message and returns False
            self.__message = "You may not use \"password\" as a password... \n"
            return False

        result = s.endswith("123")

        if result:  # if password ends with "123" then it returns False, and prints error message
            self.__message = "You may no use \"123\" at the end of your password. \n"
            return False

        result = len(s)

        if result < 8:  # if password is less than 8 characters then it returns False and prints error message
            self.__message = "That password must be 8 characters long. \n"
            return False

        # c stands for character it's checking each character to see whether is a digit and counting each digit.

        result = sum(c.isdigit() for c in s)

        if result < 2:  # if there are less than two digits in the password; it returns False and prints error message
            self.__message = "You must have at least two digits. \n"
            return False

        result = s.isalnum()

        if not result:  # if there are characters that are alphanumeric: it returns False and prints error message
            self.__message = "Your password can only contain letters and digits. \n"
            return False

        #  if it passes all these tests, then it returns True

        else:
            return True

