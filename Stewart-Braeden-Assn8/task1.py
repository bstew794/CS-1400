# Braeden Stewart
# CS 1400
# Assn-8: task 1

# This program calculates all the perfect numbers that are less than ten thousand, or in other words, the first four.

import time

start_time = time.time()

number = 1
divisors = list()
perfectNumbers = list()
numberOfPerfects = 0
count = 0
number = 6

while numberOfPerfects < 4:  # We only need to find the first four perfect numbers.
    divisors = [1]

    count += 1

    # The next bit has the program add a divisor tot he divisor list if the divisor and number have a remainder of 0.
    # And is within the range of 2 to the number, but not including the number.

    [divisors.append(divisor) for divisor in range(2, number) if number % divisor == 0]
    if sum(divisors) == number:

        # If the number being considered is a perfect number, then it will be added to the perfectNumbers list

        perfectNumbers.append(number)
        numberOfPerfects += 1  # This is to make sure that the outside loop stops after 4 prefects are found.

    number += 1
    # This measures how many iterations we go through.


print("Perfect numbers less than 10,000 are", perfectNumbers)
print("The program took", round((time.time() - start_time), 3), "seconds to run.")
print("And the inner loop took", count, "iterations!")

# End of line.....
