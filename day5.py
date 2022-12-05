import re


# Parse input
# Today's parsing was a hard one!!
def read_input():
    initial_strs = []
    initial_config = []
    commands = []
    matcher = re.compile(r'move (\d*) from (\d*) to (\d*)')

    with open("inputs/day5.txt", "r") as fin:
        reading_initial = True
        for line in fin:
            line = line.strip()
            if reading_initial:
                if line[0] != '1':
                    initial_strs.append(line)
                else:
                    n_cols = int(line[-1])
                    initial_config = [[] for _ in range(n_cols)]
                    reading_initial = False

            elif line != '':
                res = matcher.search(line)
                commands.append(tuple(map(int, res.groups())))

    def break_config(line):
        res = []
        while line != '':
            res.append(line[1])
            line = line[4:]
        return res

    for line in initial_strs[::-1]:
        content = break_config(line)
        for i, element in enumerate(content):
            if element != ' ':
                initial_config[i].append(element)

    return initial_config, commands


# PROBLEM 1: Perform cargo reassignment inverting the fragment to be moved
# (simulates transferring one element at a time from stack to stack)
def problem_1():
    initial_config, commands = read_input()
    for quantity, origin, destiny in commands:
        origin = origin - 1
        destiny = destiny - 1
        fragment = initial_config[origin][-quantity:]
        initial_config[origin] = initial_config[origin][:-quantity]
        initial_config[destiny] = initial_config[destiny] + fragment[::-1]

    return ''.join([elem[-1] for elem in initial_config])


# PROBLEM 2: Perform cargo reassignment without inverting the fragment to be
# moved (simulates transferring all elements at once from stack to stack)
def problem_2():
    initial_config, commands = read_input()
    for quantity, origin, destiny in commands:
        origin = origin - 1
        destiny = destiny - 1
        fragment = initial_config[origin][-quantity:]
        initial_config[origin] = initial_config[origin][:-quantity]
        initial_config[destiny] = initial_config[destiny] + fragment

    return ''.join([elem[-1] for elem in initial_config])


if __name__ == '__main__':
    print(problem_1())
    print(problem_2())
