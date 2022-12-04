# Parse input
def read_input():
    result = []
    with open("inputs/day4.txt", "r") as fin:
        for l in fin:
            (a, b), (c, d) = (map(lambda x: x.split("-"), l.strip().split(",")))
            result.append(((int(a), int(b)), (int(c), int(d))))
    return result


# PROBLEM 1: Check if cleaning zone of one elf is included in cleaning zone of
# the other
def problem_1():
    def outer_limits(zone1, zone2):
        return (min(zone1[0], zone2[0]), max(zone1[1], zone2[1]))

    zones = read_input()
    score = 0

    for zone1, zone2 in zones:
        score += (
            1
            if zone1 == outer_limits(zone1, zone2)
            or zone2 == outer_limits(zone1, zone2)
            else 0
        )

    return score


# PROBLEM 2: Check which intervals have non-empty intersection
def problem_2():
    zones = read_input()

    score = 0
    for zone1, zone2 in zones:
        # Ensure that zone1 starts before zone2
        if zone1[0] > zone2[0]:
            zone1, zone2 = zone2, zone1

        if zone1[1] >= zone2[0]:
            score += 1

    return score
