# Braeden Stewart
# CS 1400
# Assn 15 - task 2

# Here is my program, God help you understand what is going on as I barely am able to myself.

from deck import Deck
import time


class Dealer:
    def __init__(self):
        self.bust = False
        self.handSum = 0


class Player:
    def __init__(self):
        self.name = 0
        self.balance = 100
        self.bet = 0
        self.bust = False


def sumHand(lst):
    handSum = 0
    for i in range(len(lst)):
        rank = lst[i].getRank()

        if rank == "Queen" or rank == "King" or rank == "Jack":
            handSum += 10
        if rank == "Ace":
            handSum += 11
        if rank not in ["Queen", "King", "Jack", "Ace"]:
            handSum += lst[i].getCardValue()

    if handSum > 21:
        handSum = 0
        for i in range(len(lst)):
            rank = lst[i].getRank()

            if rank == "Queen" or rank == "King" or rank == "Jack":
                handSum += 10
            if rank == "Ace":
                handSum += 1
            if rank not in ["Queen", "King", "Jack", "Ace"]:
                handSum += lst[i].getCardValue()

    return handSum


def bustOrNot(lst):
    handSum = sumHand(lst)
    if handSum > 21:
        return True
    else:
        return False


def main():
    playAgain = True
    print("Welcome to Black Jack simulator New Vegas! \n")

    while playAgain:
        numOfPlayers = eval(input("How many players are playing?"))

        if numOfPlayers > 5:
            print("\n I'm sorry, but you can only have a max of five players \n")
            break

        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player()
        player5 = Player()
        player6 = Player()
        dealer = Dealer()

        playerLst1 = [player1, player2, player3, player4, player5, player6]
        playerLst2 = []
        badLst = []
        badPlayer = player6
        sortLst = []

        for i in range(numOfPlayers):
            playerLst1[i].name = i + 1
            playerLst2.append(playerLst1[i])
            sortLst.append(playerLst1[i])

        while playAgain:
            playerLst1.remove(badPlayer)

            deck = Deck()

            for i in range(len(playerLst2)):
                temp = True
                while temp:
                    message = "\n Player" + str(playerLst2[i].name) + ", Your current balance is: $" + str(playerLst2[i].balance)
                    print(message)
                    playerLst2[i].bet = eval(input("how much do you want to bet?"))

                    if playerLst2[i].balance < 5:
                        if playerLst2[i].bet < playerLst2[i].balance:
                            print("\n You must bet your whole balance if it is under the minimum bid of $5")
                            continue
                    elif playerLst2[i].bet < 5:
                        print("\n You must bet at least $5.")
                        continue
                    elif playerLst2[i].bet > playerLst2[i].balance:
                        print("\n Silly Rabbit, money is for rich people!")
                    else:
                        temp = False

            hands = []

            for row in range(len(playerLst2) + 1):
                hands.append([])
            for column in range(2):
                for i in range(len(playerLst2) + 1):
                    hands[i].append(deck.draw())

            dealerReveal = hands[len(playerLst2) - 1][1]
            print("\n The dealer's second card is:", dealerReveal)

            for i in range(len(playerLst2)):
                temp = True
                while temp:
                    print("\n Player", str(playerLst2[i].name), "Your hand holds these cards:", hands[i])

                    bustVar = bustOrNot(hands[i])

                    if bustVar:
                        print("\n You busted")
                        playerLst2[i].bust = True
                        break

                    userInput = input("\n Hit or Hold?")

                    if userInput == "Hold":
                        break

                    hands[i].append(deck.draw())

            temp = True

            while temp:
                message1 = "\n Dealer draws a card."
                message2 = "\n Dealer holds."
                message3 = "\n Dealer busts."

                time.sleep(1)

                if sumHand(hands[len(playerLst2)]) > 21:
                    dealer.bust = True
                    print(message3)
                    break
                elif sumHand(hands[len(playerLst2)]) >= 17:
                    dealer.handSum = sumHand(hands[len(playerLst2)])
                    print(message2)
                    break
                elif sumHand(hands[len(playerLst2)]) < 17:
                    hands[len(playerLst2)].append(deck.draw())
                    print(message1)

            for i in range(len(playerLst2)):
                if dealer.handSum < sumHand(hands[i]):
                    if not playerLst2[i].bust:
                        playerLst2[i].balance += playerLst2[i].bet
                        print("\n Player", str(playerLst2[i].name), ", you win!")
                if not playerLst2[i].bust and dealer.handSum == sumHand(hands[i]):
                    print("\n Player", str(playerLst2[i].name), ", you tied with the dealer")
                if not playerLst2[i].bust and dealer.bust:
                    playerLst2[i].balance += playerLst2[i].bet
                    print("\n Player", str(playerLst2[i].name), ", you win!")
                if not dealer.bust and dealer.handSum > sumHand(hands[i]):
                    print("\n Player", str(playerLst2[i].name), ", you lost")
                    playerLst2[i].balance -= playerLst2[i].bet
                    if playerLst2[i].balance < 0:
                        playerLst2[i].balance = 0

                if playerLst2[i].bust:
                    print("\n Player", str(playerLst2[i].name), ", you lost")

                    playerLst2[i].balance -= playerLst2[i].bet
                    if playerLst2[i].balance < 0:
                        playerLst2[i].balance = 0

                print("\n Your balance is now $", playerLst2[i].balance)

            for i in range(len(playerLst1)):
                if playerLst1[i].balance == 0:
                    badPlayer = playerLst1[i]
                    badLst.append(playerLst1[i])
                    playerLst2.remove(playerLst1[i])

            userInput2 = input("\n Play again? [Y/N]")

            if userInput2 == "N":
                playAgain = False

                for i in range(numOfPlayers - 1):
                    currentMax = sortLst[i]
                    currentMaxIndex = i

                    for j in range(i + 1, numOfPlayers):
                        if currentMax.balance < sortLst[j].balance:
                            currentMax = sortLst[j]
                            currentMaxIndex = j

                        if currentMaxIndex != i:
                            sortLst[currentMaxIndex] = sortLst[i]
                            sortLst[i] = currentMax

                print("\n Thank Y'all for playing")

                for i in range(numOfPlayers):
                    message = str(sortLst[i].name) + ": $" + str(sortLst[i].balance)
                    print(message)


main()