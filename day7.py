from collections import defaultdict


def read_input():
    paths = defaultdict(int)
    curr_path = []
    with open("inputs/day7.txt", "r") as fin:
        for line in fin:
            splits = line.strip().split(" ")
            if splits[1] == 'cd':
                if splits[2] == '..':
                    curr_path = curr_path[:-1]
                else:
                    curr_path.append(splits[2])
            elif splits[1] == 'ls':
                continue
            elif splits[0] == 'dir':
                continue
            else:
                for i in range(1, len(curr_path)+1):
                    paths["/".join(curr_path[:i])] += int(splits[0])

    return paths


def problem_1():
    paths = read_input()
    acc = 0
    for size in paths.values():
        if size < 100000:
            acc += size

    return acc


def problem_2():
    paths = read_input()
    unused_space = 70000000  - paths['/']
    needed_space = 30000000 - unused_space
    return min(filter(lambda x: x > needed_space, paths.values()))


problem_1()
problem_2()
