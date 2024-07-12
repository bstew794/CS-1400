# Braeden Stewart
# CS 1400
# Assn-5: Task 2

# This program

print("Welcome to Financial Internal, now you've got a friend in the debt business.")
print("If you will fill out the form below, then we can help you predict your future...")
print("Financial future, of course.")
print("")

investmentAmount = eval(input("Please enter your investment amount in USD:"))
annualInterestRate = eval(input("Enter your annual interest rate percentage:"))
numberOfYears = eval(input("Lastly, please enter the number of years:"))

monthlyInterestRate = (annualInterestRate / 100) / 12
numberOfMonths = numberOfYears * 12

futureInvestmentValue = round((investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths) * 100)/ 100.0

print("")
print("Your future investment value is", futureInvestmentValue, "USD.")