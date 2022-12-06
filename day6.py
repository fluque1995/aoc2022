def read_input():
    with open("inputs/day6.txt", "r") as fin:
        input_str = fin.read().strip()

    return input_str


def find_distinct(inp, length):
    for i in range(len(inp)):
        if len(set(inp[i:i+length])) == length:
            return i + length


def problem_1():
    return find_distinct(read_input(), 4)


def problem_2():
    return find_distinct(read_input(), 14)


print(problem_1())
print(problem_2())
