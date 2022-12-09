def read_input():
    with open("inputs/day9.txt", "r") as fin:
        return [(l.strip().split()[0], int(l.strip().split()[1])) for l in fin]


class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return P(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"P({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(repr(self))


class Rope:
    DIRS = {'U': P(0, 1), 'D': P(0, -1), 'L': P(-1, 0), 'R': P(1, 0)}

    def __init__(self, length):
        self.nodes = [P(0, 0) for _ in range(length)]
        self.visits = set([P(0, 0)])

    def pull(self, i, j):
        diff = self.nodes[i] - self.nodes[j]
        if diff.x > 1:
            self.nodes[j] += Rope.DIRS['R']
            if diff.y > 0:
                self.nodes[j] += Rope.DIRS['U']
            elif diff.y < 0:
                self.nodes[j] += Rope.DIRS['D']
        elif diff.x < -1:
            self.nodes[j] += Rope.DIRS['L']
            if diff.y > 0:
                self.nodes[j] += Rope.DIRS['U']
            elif diff.y < 0:
                self.nodes[j] += Rope.DIRS['D']
        elif diff.y > 1:
            self.nodes[j] += Rope.DIRS['U']
            if diff.x > 0:
                self.nodes[j] += Rope.DIRS['R']
            elif diff.x < 0:
                self.nodes[j] += Rope.DIRS['L']
        elif diff.y < -1:
            self.nodes[j] += Rope.DIRS['D']
            if diff.x > 0:
                self.nodes[j] += Rope.DIRS['R']
            elif diff.x < 0:
                self.nodes[j] += Rope.DIRS['L']

    def move(self, direction, steps):
        for _ in range(steps):
            self.nodes[0] += Rope.DIRS[direction]
            for i in range(len(self.nodes) - 1):
                self.pull(i, i+1)
            self.visits.add(self.nodes[-1])


def problem_1():
    directions = read_input()
    rope = Rope(2)
    [rope.move(d, s) for d, s in directions]
    return len(rope.visits)


def problem_2():
    directions = read_input()
    rope = Rope(10)
    [rope.move(d, s) for d, s in directions]
    return len(rope.visits)


if __name__ == '__main__':
    print(problem_1())
    print(problem_2())
