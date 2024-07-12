# Braeden Stewart
# CS 1400
# Assn 14 - task 3

# This file contains the definitions and functions for the Card, and Deck class

import random

mano = ["Rock", "Paper", "Scissors"]
coin = ["Heads", "Tails"]
maxCardValue = 20


class Card:
    def __init__(self, cardID):
        self.__mano = 0
        self.__coin = 0

        if cardID % 2 != 0:  # coin cannot have a a value if the id is an even number
            self.__coin = 1
        if (cardID // 2) > 19:  # the id, and cardValue cannot be negative so cardID / 2 must be > 19 or 39
            self.__mano = 1
            if (cardID // 2) > 39:
                self.__mano = 2

        self.__value = (cardID / 2) - (self.__coin / 2) - (20 * self.__mano) + 1  # a rework of formula below
        self.__id = 2 * ((self.__value - 1) + (maxCardValue * self.__mano)) + self.__coin  # stores cardID

    # The next few functions access the values stored in the Card class

    def getCardValue(self):
        return self.__value

    def getCardMano(self):
        return mano[self.__mano]

    def getCardCoin(self):
        return coin[self.__coin]

    def getCardId(self):
        return self.__id


class Deck:
    def __init__(self):
        self.__deck = []  # creates a list for future use

    def __generateDeck(self):
        for i in range(0, 120):
            card = Card(i)

            if card.getCardValue() > 0:  # had issues with card values of zero, so I used this to remove them.
                self.__deck.append(card)

    def shuffle(self):
        self.__deck = []
        self.__generateDeck()

        random.shuffle(self.__deck)

    def draw(self, index):  # draws a card from the deck
        return self.__deck[index - 1]

    def displayDeck(self):  # for testing purposes, I don't dare remove it now.
        for i in range(0, 120):
            displayCard = self.__deck[i]

            print(displayCard.getCardValue(), "of", displayCard.getCardMano(), displayCard.getCardCoin(), "\n")


# Make sure you understand this to do the opposite conversion!!!


def convertCardToValue(cardValue, cardMano, cardCoin):
    return 2 * ((cardValue - 1) + (maxCardValue * mano.index(cardMano))) + coin.index(cardCoin)
