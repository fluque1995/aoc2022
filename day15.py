import re
import time

from collections import defaultdict


def read_input():
    matcher = re.compile(
        r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)"
    )
    pairs = []
    with open("inputs/day15.txt", "r") as fin:
        for line in fin:
            matches = matcher.search(line.strip())
            x_sensor, y_sensor, x_beacon, y_beacon = map(int, matches.groups())
            pairs.append(((y_sensor, x_sensor), (y_beacon, x_beacon)))

    return pairs


def manhattan(start, end):
    (st_i, st_j), (end_i, end_j) = start, end
    return abs(end_i - st_i) + abs(end_j - st_j)


def intersect(lhs, rhs):
    if lhs[0] > rhs[0]:
        lhs, rhs = rhs, lhs

    lmin, lmax = lhs
    rmin, rmax = rhs
    if lmax >= rmin - 1:
        return (lmin, max(lmax, rmax)), None
    else:
        return lhs, rhs


def intersect_row(row_list, new_value):
    curr_value = new_value
    new_list = []
    for element in row_list:
        first, second = intersect(element, curr_value)
        if second is None:
            curr_value = first
        else:
            new_list.append(first)
            curr_value = second
    else:
        new_list.append(curr_value)

    return new_list


def print_maze(rows, size):
    maze = [["." for _ in range(size+1)] for _ in range(size+1)]
    for i in rows.keys():
        if 0 <= i <= size:
            for pair in rows[i]:
                for j in range(pair[0], pair[1]+1):
                    if 0 <= j <= size:
                        maze[i][j] = '#'

    for i, row in enumerate(maze):
        print(f"{i:02} {''.join(row)}")


def problem_2(size):
    inp = read_input()
    rows = defaultdict(list)

    for signal, beacon in inp:
        dist = manhattan(signal, beacon)
        min_i, max_i = max(0, signal[0] - dist), min(size, signal[0] + dist)
        for i in range(min_i, max_i + 1):
            rem_dist = dist - abs(i - signal[0])
            min_j, max_j = max(0, signal[1] - rem_dist), min(size, signal[1] + rem_dist)
            rows[i] = intersect_row(rows[i], (min_j, max_j))

    for (s_i, s_j), (b_i, b_j) in inp:
        if 0 <= s_i <= size and 0 <= s_j <= size:
            rows[s_i] = intersect_row(rows[s_i], (s_j, s_j))
        if 0 <= b_i <= size and 0 <= b_j <= size:
            rows[b_i] = intersect_row(rows[b_i], (b_j, b_j))

    for row, cols in rows.items():
        if len(cols) > 1:
            return (cols[0][1] + 1) * size + row


def problem_1(row):
    row_blocks = []
    inp = read_input()
    for sensor, beacon in inp:
        dist = manhattan(sensor, beacon)
        vertical_dist = abs(sensor[0] - row)
        if vertical_dist < dist:
            disp = abs(vertical_dist - dist)
            down = sensor[1] - disp
            up = sensor[1] + disp
            row_blocks = intersect_row(row_blocks, (down, up))

    return sum([up - down + 1 for (down, up) in row_blocks])


if __name__ == '__main__':
    st = time.time()
    print(problem_1(2_000_000))
    end_1 = time.time()
    print(problem_2(4_000_000))
    print(f"Times: problem 1 - {end_1 - st}, problem 2 - {time.time() - end_1}")
