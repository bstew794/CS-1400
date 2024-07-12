# Braeden Stewart
# CS 1400
# Assn 14 - Task 1

# This program asks for a user to input numbers until satisfied which inputted to a list and then processed


def main():
    playAgain = True
    numList = []

    while playAgain:
        userInput = input("\n Please give me a number or simply press enter to finish input. \n")

        if userInput == "":
            break

        numList.append(eval(userInput))

    lenList = len(numList)
    maxValue = max(numList)
    minValue = min(numList)

    count = 0
    sumList = 0

    while count < lenList:
        sumList += numList[count]
        count += 1

    avgValue = sumList / lenList

    print("Length of list:", lenList, "\n Max value:", maxValue, "\n Min value:", minValue, "\n Sum of list items:",
          sumList, "\n Average value:", avgValue)

    print(numList[0])


main()
