import string

# Parse input
def read_input():
    with open("inputs/day3.txt", "r") as fin:
        return [l.strip() for l in fin]


# PROBLEM 1: Find the repeated char in both parts of string
def problem_1():
    rucksacks = read_input()
    alphabet = list(string.ascii_letters)
    score = 0
    for content in rucksacks:
        c1, c2 = set(content[:len(content)//2]), set(content[len(content)//2:])
        (common,) = c1.intersection(c2)
        score += alphabet.index(common) + 1

    return score


# PROBLEM 2: Find the repeated char in each group of three rucksacks
def problem_2():
    rucksacks = read_input()
    alphabet = list(string.ascii_letters)
    score = 0
    for r1, r2, r3 in zip(rucksacks[0::3], rucksacks[1::3], rucksacks[2::3]):
        c1, c2, c3 = set(r1), set(r2), set(r3)
        (common,) = c1.intersection(c2).intersection(c3)
        score += alphabet.index(common) + 1

    return score


if __name__ == '__main__':
    print(problem_1())
    print(problem_2())
