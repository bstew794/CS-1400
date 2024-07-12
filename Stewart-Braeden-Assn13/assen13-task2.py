# Braeden Stewart
# CS 1400
# Assn 13 - task 2

# This program randomly generates a integer from 0 to 9 a total of 1,000 times
# and then counts the occurrences of each integer (0 to nine) of the 1,000 times.

import random
iterations = 0
numberList = []

while iterations <= 1000:
    number = random.randint(0, 9)
    numberList.append(number)
    iterations += 1

integer = 0
counts = []

while integer <= 9:
    count = numberList.count(integer)
    counts.append(count)

    integer += 1

print("number of zeros, ones, twos, threes, fours, fives, sixes, sevens, eights, nines (respectively):", counts)
