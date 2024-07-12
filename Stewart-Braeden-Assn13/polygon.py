# Braeden Stewart
# CS 1400
# Assn 13 - task 1

# This file contains the methods for the class Polygon.


class Polygon:
    def __init__(self, numberOfSides):
        self.__sides = numberOfSides

    def __add__(self, p2):
        return self.__sides + p2.__sides

    def __sub__(self, p2):
        return self.__sides - p2.__sides

    def __lt__(self, p2):
        temp = self.__sides - p2.__sides

        if temp > 0 or temp == 0:
            return False
        else:
            return True

    def __gt__(self, p2):
        temp = self.__sides - p2.__sides

        if temp < 0 or temp == 0:
            return False
        else:
            return True

    def __eq__(self, p2):
        temp = self.__sides - p2.__sides

        if temp < 0 or temp > 0:
            return False
        else:
            return True

    def __len__(self):

        temp = [self.__sides]
        return len(temp)

    def __str__(self):
        temp = self.__sides
        return str(temp)
