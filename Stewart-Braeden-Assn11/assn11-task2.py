# Braeden Stewart
# CS 1400
# Assn 11 - task 2

from account import *


def main():
    repeat1 = False
    id = 0
    balance = 0
    annualInterestRate = 0

    while not repeat1:
        id, balance, annualInterestRate = eval(input("Please give me an ID, balance, and annual interest rate: \n"))

        if id < 0 or balance < 0 or annualInterestRate < 0:
            print("Negative numbers are not accepted, please try again. \n")
        if annualInterestRate > 10:
            print("You cannot have an annual interest rate higher than 10, please try again. \n")
        else:
            break

    account = Account(id, balance, annualInterestRate)
    repeat2 = False

    while not repeat2:
        print("(1:) Display ID \n (2:) Display Balance \n (3:) Display Annual Interest Rate \n "
              "(4:) Display Monthly Interest Rate \n (5:) Display Monthly Interest \n (6:) Withdraw Money \n "
              "(7:) Deposit Money \n (8:) Exit \n ")

        choice = eval(input("What do you want to do? \n"))

        if choice == 8:
            break
        elif choice == 1:
            print("Your account id is:", account.getId(), "\n")
        elif choice == 2:
            print("Your current balance is:", account.getBalance(), "\n")
        elif choice == 3:
            print("Your Annual Interest Rate is:", account.getannualInterestRate(), "\n")
        elif choice == 4:
            print("Your monthly interest rate is:", account.getMonthlyInterestRate(), "\n")
        elif choice == 5:
            print("Your monthly interest is:", account.getMonthlyInterest(), "\n")
        elif choice == 6:
            amount = eval(input("How much would you like to withdraw?"))

            account.withdraw(amount)

            print("You now have", account.getBalance(), "in your account. \n")

        elif choice == 7:
            amount = eval(input("How much would you like to deposit?"))

            account.deposit(amount)

            print("You now have", account.getBalance(), "in your account. \n")

        else:
            print("I am sorry that is not a valid input \n")

    print("Goodbye!")



main()

# End of line...