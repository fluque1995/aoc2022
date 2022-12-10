def read_input():
    ops = []
    with open("inputs/day10.txt", "r") as fin:
        for line in fin:
            line_split = line.strip().split(" ")
            if line_split[0] == 'noop':
                ops.append(('noop', None))
            else:
                ops.append((line_split[0], int(line_split[1])))

    return ops


def problem_1():
    registry = 1
    signal = 0
    steps = 0
    for op, val in read_input():
        if op == 'noop':
            steps += 1
            if steps % 40 == 20:
                signal += registry * steps
        else:
            steps += 2
            if steps % 40 in [20, 21]:
                signal += registry * (40*(steps // 40) + 20)
            registry += val

    return signal


def print_sprite(sprite):
    for line in sprite:
        print("".join(line))


def position(i):
    return i // 40, i % 40 - 1


def problem_2():
    sprite = [['.' for _ in range(40)] for _ in range(6)]
    registry = 1
    steps = 0
    for op, val in read_input():
        if op == 'noop':
            steps += 1
            line, pos = position(steps)
            if pos in range(registry - 1, registry + 2):
                sprite[line][pos] = '#'
        else:
            steps += 2
            line, pos = position(steps)
            if pos - 1 in range(registry - 1, registry + 2):
                sprite[line][pos-1] = '#'
            if pos in range(registry - 1, registry + 2):
                sprite[line][pos] = '#'

            registry += val

    return sprite


print_sprite(problem_2())
