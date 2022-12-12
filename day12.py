import time

from dataclasses import dataclass
from queue import PriorityQueue


def read_input(start_points):
    result = []
    starting_points = []
    with open("inputs/day12.txt", "r") as fin:
        for i, line in enumerate(fin):
            result.append([])
            for j, elem in enumerate(line.strip()):
                if elem in start_points:
                    starting_points.append((i, j))
                    result[i].append(0)
                elif elem == "E":
                    ending_point = i, j
                    result[i].append(ord("z") - ord("a"))
                else:
                    result[i].append(ord(elem) - ord("a"))

    return result, starting_points, ending_point


@dataclass(order=True)
class ClimbPath:
    curr_distance: int
    position: (int, int)


class Climber:
    def __init__(self, heights, start_point, end_point):
        self.heights = heights
        self.start_point = ClimbPath(0, start_point)
        self.end_point = end_point
        self.open_nodes = PriorityQueue()
        self.open_nodes.put((self.cost(self.start_point), self.start_point))
        max_dist = len(heights) * len(heights[0])
        self.curr_distances = [[max_dist for _ in heights[0]] for _ in heights]

    def cost(self, point):
        return point.curr_distance + self.heuristic_cost(point)

    def heuristic_cost(self, point):
        return abs(point.position[0] - self.end_point[0]) + abs(
            point.position[1] - self.end_point[1]
        )

    def is_valid_path(self, old_p, new_p):
        old_i, old_j = old_p.position
        new_i, new_j = new_p.position
        return (
            0 <= new_i < len(self.heights)
            and 0 <= new_j < len(self.heights[0])
            and self.heights[old_i][old_j] + 1 >= self.heights[new_i][new_j]
            and new_p.curr_distance < self.curr_distances[new_i][new_j]
        )

    def step(self):
        try:
            curr_path = self.open_nodes.get(block=False)[1]
        except:
            return True, None
        curr_dist = curr_path.curr_distance
        curr_i, curr_j = curr_path.position
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_path = ClimbPath(curr_dist + 1, (curr_i + i, curr_j + j))
            if self.is_valid_path(curr_path, new_path):
                if new_path.position == self.end_point:
                    return True, new_path.curr_distance
                else:
                    self.curr_distances[new_path.position[0]][new_path.position[1]] = curr_dist + 1
                    self.open_nodes.put((self.cost(new_path), new_path))

        return False, None

    def climb(self):
        end, distance = False, None
        while not end:
            end, distance = self.step()

        return distance


def problem_1():
    heights, (start_point,), end_point = read_input(['S'])
    climber = Climber(heights, start_point, end_point)
    return climber.climb()


def problem_2():
    heights, start_points, end_point = read_input(['S', 'a'])
    steps = []
    for i, start_point in enumerate(start_points):
        climber = Climber(heights, start_point, end_point)
        distance = climber.climb()
        if distance is not None:
            steps.append(distance)

    return min(steps)


print(problem_1())
print(problem_2())
