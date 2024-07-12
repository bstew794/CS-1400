# Braeden Stewart
# CS 1400
# Assn 15 - task 1

# This program sorts a users hand using either a bubble sort or insertion sort

from deck import Deck


def printNicknames(count, lst):
    nickNames = []

    for i in range(0, 19):
        card = lst[i]
        temp = card.getNickName()
        nickNames.append(temp)

    print(count, ":", nickNames)


def main():
    deck = Deck()
    hand = []

    for i in range(1, 20):
        hand.append(deck.draw())

    userInput = input("do you want to use Bubble or Insertion to sort your hand?")

    if userInput == "Bubble":
        count = 1
        n = len(hand)

        for i in range(n):
            for j in range(0, n - i - 1):
                if hand[j].getCardValue() > hand[j + 1].getCardValue():
                    printNicknames(count, hand)
                    count += 1

                    hand[j], hand[j + 1] = hand[j + 1], hand[j]

        printNicknames(count, hand)

    elif userInput == "Insertion":
        count = 1
        printNicknames(count, hand)

        for i in range(0, len(hand)):
            currentElement = hand[i]
            k = i - 1
            while k >= 0 and hand[k].getCardValue() > currentElement.getCardValue():
                hand[k + 1] = hand[k]
                k -= 1

            hand[k + 1] = currentElement

            count += 1
            printNicknames(count, hand)


main()