# Braeden Stewart
# CS 1400
# Assn-6: Task 2

# This program prompts the user for the input of an employee's name, pay rate, weekly hours, and the relevant tax rate
# The program then calculates the net pay and displays all the relevant information

employeeName = input("Enter employee's name:")
weeklyHours = abs(eval(input("Enter hours worked in a week:")))
payRate = abs(eval(input("Enter employee's hourly pay rate:")))
federalTaxRate = abs(eval(input("Enter federal tax withholding rate:")))
stateTaxRate = abs(eval(input("Enter state tax withholding rate:")))

stringFW = format(federalTaxRate, ".1%")
stringSW = format(stateTaxRate, ".1%")

outputName = format(employeeName + " pay information", "^40s")

grossPay = payRate * weeklyHours

federalWithholding = federalTaxRate * grossPay
stateWithholding = stateTaxRate * grossPay

formatedFW = "Federal Withholding (" + str(stringFW) + "): $"
formatedSW = "State Withholding (" + str(stringSW) + "): $"

totalDeductions = federalWithholding + stateWithholding

netPay = grossPay - totalDeductions

output = "\n" + outputName.upper() + "\n" + "\n"
output += format("pay", "^40s") + "\n"
output += format("Hours Worked:", ">38s") + format(weeklyHours, "14") + "\n"
output += format("Pay Rate: $", ">40s") + format(payRate, "12.2f") + "\n"
output += format("Gross Pay: $", ">40s") + format(grossPay, "12.2f") + "\n" + "\n"
output += format("Deductions", "^40s") + "\n"
output += format(formatedFW, ">40s") + format(federalWithholding, "12.2f") + "\n"
output += format(formatedSW, ">40s") + format(stateWithholding, "12.2f") + "\n"
output += format("Total Deduction: $", ">40s") + format(totalDeductions, "12.2f") + "\n" + "\n"
output += format("Net Pay: $", ">40s") + format(netPay, "12.2f")

print(output)

# END OF LINE...