# Braeden Stewart
# CS 1400
# Assn 13 - task 1

# This program tests if I overloaded the operators properly using two polygon objects.

from polygon import Polygon


def main():
    userInput1 = eval(input("Please give me how many sides the first polygon has:"))
    userInput2 = eval(input("Please give me how many sides the second polygon has:"))
    polygon1 = Polygon(userInput1)
    polygon2 = Polygon(userInput2)

    addResult = polygon1 + polygon2
    subResult = polygon1 - polygon2
    ltResult = polygon1 < polygon2
    gtResult = polygon1 > polygon2
    eqResult = polygon1 == polygon2
    lenResult1 = len(polygon1)
    lenResult2 = len(polygon2)
    strResult1 = str(polygon1)
    strResult2 = str(polygon2)

    print(addResult, subResult, ltResult, gtResult, eqResult, lenResult1, lenResult2, strResult1, strResult2)


main()