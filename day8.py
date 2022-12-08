import itertools


def read_input():
    with open("inputs/day8.txt") as fin:
        return [list(map(int, [*l.strip()])) for l in fin]


def horiz_visible(trees, left):
    row_range = range(len(trees[0])) if left else range(len(trees[0]) - 1, -1, -1)
    visible = [[False] * len(trees[0]) for _ in trees]
    for i, line in enumerate(trees):
        curr_height = -1
        for j in row_range:
            elem = line[j]
            if elem > curr_height:
                visible[i][j] = True
                curr_height = elem

    return visible


def vert_visible(trees, top):
    visible = [[False] * len(trees[0]) for _ in trees]
    col_range = range(len(trees)) if top else range(len(trees) - 1, -1, -1)
    for i in range(len(trees[0])):
        curr_height = -1
        for j in col_range:
            elem = trees[j][i]
            if elem > curr_height:
                visible[j][i] = True
                curr_height = elem

    return visible


def problem_1():
    trees = read_input()
    left, right = horiz_visible(trees, True), horiz_visible(trees, False)
    top, bottom = vert_visible(trees, True), vert_visible(trees, False)
    acc = 0
    for a, b, c, d in zip(left, right, top, bottom):
        for a1, b1, c1, d1 in zip(a, b, c, d):
            acc += 1 if (a1 or b1 or c1 or d1) else 0

    return acc


def scenic_score(trees, i, j):
    def visual(rng, horizontal):
        acc = 0
        for l in rng:
            acc += 1
            if (trees[i][l] >= trees[i][j] and horizontal) or (
                trees[l][j] >= trees[i][j] and not horizontal
            ):
                return acc
        return acc

    lview = visual(range(j - 1, -1, -1), True)
    rview = visual(range(j + 1, len(trees[0])), True)
    tview = visual(range(i - 1, -1, -1), False)
    bview = visual(range(i + 1, len(trees)), False)
    return lview * rview * tview * bview


def problem_2():
    trees = read_input()
    return max(
        scenic_score(trees, i, j)
        for i, j in itertools.product(range(len(trees)), range(len(trees[0])))
    )


if __name__ == "__main__":
    print(problem_1())
    print(problem_2())
