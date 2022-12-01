# AUXILIAR FUNCTION: Input processing
def read_input():
    with open("inputs/day1.txt") as fin:
        lines = [line.strip() for line in fin]

    return lines


# PROBLEM 1: Given a list of groups of integers (each group is separated by an
# empty line), get the max sum of the groups

# IDEA: Get the sum of each group and search the maximum in the result
def problem1():
    kalories_list = read_input()
    accs = [0]
    for value in kalories_list:
        if value:
            accs[-1] += int(value)
        else:
            accs.append(0)

    return max(accs)

# PROBLEM 2: Given the same list, get the sum of the top three greatest values

# IDEA: Given the sum of each group (same as before), compute the top-3 values
# and add them up
def problem2():
    kalories_list = read_input()
    accs = [0]
    for value in kalories_list:
        if value:
            accs[-1] += int(value)
        else:
            accs.append(0)

    max1, max2, max3 = 0, 0, 0

    for value in accs:
        if value >= max1:
            max1, max2, max3 = value, max1, max2
        elif value >= max2:
            max2, max3 = value, max2
        elif value >= max3:
            max3 = value

    return max1 + max2 + max3


if __name__ == '__main__':
    print(problem1())
    print(problem2())
