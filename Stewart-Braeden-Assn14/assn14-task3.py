# Braeden Stewart
# CS 1400
# Assn 14 - task 3

# This program simulates the fictional card game of Gubbins

from gubbinsutil import Deck
from gubbinsutil import convertCardToValue


def main():
    print("Welcome to Gubbins! Please wait while your deck is assembled and shuffled")

    deck = Deck()
    deck.shuffle()  # invokes deck shuffling
    hand = []

    addToHand(hand, deck)  # creates player hand

    playAgain = True

    while playAgain:

        print("\n 1. Sort by value \n 2. Sort by ID \n 3. Find card \n 4. New hand \n 5. Quit")
        userInput = eval(input("\n What do you choose? \n "))

        if userInput == 1:
            hand = valueSort(hand)

            displayHand(hand)

        elif userInput == 2:
            hand = sortID(hand)

            displayHand(hand)

        elif userInput == 3:
            value = eval(input("Enter the card value:"))
            mano = input("Enter the card Mano:")
            coin = input("Enter the card Coin:")
            ident = convertCardToValue(value, mano, coin)

            sortID(hand)

            if findCard(ident, hand):
                print("The card is in your hand!!! \n")
            else:
                print("The card is not in your hand. \n")

        elif userInput == 4:
            hand = []
            deck.shuffle()

            addToHand(hand, deck)

        elif userInput == 5:
            print("\n Goodbye!")
            break


def valueSort(series):
    hand = series

    for i in range(30):
        minIndex = i

        for j in range(i + 1, 30):
            lowCard = hand[minIndex]  # grabs the lower index from hand
            highCard = hand[j]  # grabs the higher index of the hand list

            lowValue = lowCard.getCardValue()
            highValue = highCard.getCardValue()

            if lowValue > highValue:  # compares lower and higher card values and switches if necessary
                minIndex = j

        hand[i], hand[minIndex] = hand[minIndex], hand[i]

    return hand


def sortID(series):
    hand = series

    for i in range(len(hand)):
        minIndex = i

        for j in range(i + 1, len(hand)):
            lowCard = hand[minIndex]  # grabs the lower index from hand
            highCard = hand[j]  # grabs the higher index of the hand list

            lowValue = lowCard.getCardId()  # grabs id from lower index
            highValue = highCard.getCardId()  # grabs id from higher index

            if lowValue > highValue:  # compares the two values, and switches them if necessary
                minIndex = j

        hand[i], hand[minIndex] = hand[minIndex], hand[i]

    return hand


def displayHand(series):  # displays the current hand
    hand = series

    for i in range(30):
        displayCard = hand[i]

        print(displayCard.getCardValue(), "of", displayCard.getCardMano(), displayCard.getCardCoin())


def addToHand(series, deck):  # adds cards to hand
    hand = series

    for i in range(30):
        card = deck.draw(i)
        hand.append(card)

    return hand


def findCard(ident, hand):  # checks to see if chosen card is in the user's hand
    low = 0
    high = len(hand) - 1

    while high >= low:  # repeats loop until the two sides of the list coincide
        mid = (low + high) // 2
        comp = hand[mid]  # temporary variable to access index mid from hand and is used later to get the id

        if ident < comp.getCardId():
            high = mid - 1  # decreases mid value each loop
        elif ident == comp.getCardId():
            return True  # ends loop and returns true if card is found amongst hand
        else:
            low = mid + 1  # raises mid value each loop

    return False  # ends loop and returns false if card is not found


main()
