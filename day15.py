import re


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
    if lmax > rmin:
        return (lmin, rmax), None
    else:
        return lhs, rhs


def check_row(sensors_list, row_ind):
    covered_indices = set()
    for sensor, beacon in sensors_list:
        dist = manhattan(sensor, beacon)
        vertical_dist = abs(sensor[0] - row_ind)
        if vertical_dist < dist:
            disp = abs(vertical_dist - dist)
            down = sensor[1] - disp
            up = sensor[1] + disp + 1
            covered_indices.update(range(down, up))

    for sensor, beacon in sensors_list:
        if sensor[0] == row_ind and sensor[1] in covered_indices:
            covered_indices.remove(sensor[1])
        if beacon[0] == row_ind and beacon[1] in covered_indices:
            covered_indices.remove(beacon[1])

    return covered_indices


def problem_1():
    inp = read_input()
    indices = check_row(inp, 2000000)
    return len(indices)


print(problem_1())
