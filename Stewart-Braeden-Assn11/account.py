# Braeden Stewart
# CS 1400
# Assn 11 - task 2

# This program contains all the functions required for the Account class to then be used in assn11-task2.py


class Account:
    def __init__(self, id = 0, balance = 100, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getannualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        self.__monthlyInterestRate = (self.__annualInterestRate / 12)
        return self.__monthlyInterestRate

    def getMonthlyInterest(self):
        self.__monthlyInterest = self.__balance * (self.__monthlyInterestRate / 100)
        return self.__monthlyInterest

    def withdraw(self, amount = 0):
        balance = self.__balance - amount

        self.__balance = balance

    def deposit(self, amount = 0):
        balance = self.__balance - amount

        self.__balance = balance

# End of line...