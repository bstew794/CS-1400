# Braeden Stewart
# CS 1400
# Assn 14 - Task

# This program prints three lists derived from a base list according to specified conditions


def main():
    baseList = list(range(1, 101))

    list1 = [x for x in baseList if x % 2 == 0]
    print(list1)

    list2 = [x for x in baseList[:50] if x % 3 == 0]
    print(list2)

    list3 = [(10 * x) for x in baseList[50:] if x % 5 == 0]
    print(list3)


main()
