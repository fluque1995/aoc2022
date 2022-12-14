import os
import time


def read_input():
    walls_list = []
    min_col, max_col, max_row = 500, 0, 0

    with open("inputs/day14.txt", "r") as fin:
        for line in fin:
            line = line.strip().split(" -> ")
            walls = []
            for pair in line:
                col, row = map(int, pair.split(","))
                if col < min_col:
                    min_col = col
                if col > max_col:
                    max_col = col
                if row > max_row:
                    max_row = row

                walls.append((row, col))
            walls_list.append(walls)

    walls_list = [[(i, j - min_col) for i, j in line] for line in walls_list]

    return walls_list, max_row, max_col - min_col, 500 - min_col


def create_maze(walls_list, nrows, ncols):
    maze = [[0 for _ in range(ncols + 1)] for _ in range(nrows+1)]

    for walls in walls_list:
        for (st_i, st_j), (end_i, end_j) in zip(walls[:-1], walls[1:]):
            if st_i != end_i:
                st_i, end_i = min(st_i, end_i), max(st_i, end_i)
                for i in range(st_i, end_i + 1):
                    maze[i][st_j] = 1
            if st_j != end_j:
                st_j, end_j = min(st_j, end_j), max(st_j, end_j)
                for j in range(st_j, end_j + 1):
                    maze[st_i][j] = 1

    return maze


def print_maze(maze):
    os.system("clear")
    for line in maze:
        print("".join(["." if e == 0 else "#" if e == 1 else "o" for e in line]), flush=False)
    time.sleep(0.03)
    print("", flush=True)


def problem_1(out=False):
    walls_list, nrows, ncols, pouring = read_input()
    maze = create_maze(walls_list, nrows, ncols)
    keep_pouring = True
    sand = 0
    while keep_pouring:
        curr_i, curr_j = 0, pouring
        try:
            while True:
                if maze[curr_i+1][curr_j] == 0:
                    curr_i += 1
                elif maze[curr_i + 1][curr_j - 1] == 0:
                    curr_i, curr_j = curr_i + 1, curr_j - 1
                elif maze[curr_i + 1][curr_j + 1] == 0:
                    curr_i, curr_j = curr_i + 1, curr_j + 1
                else:
                    maze[curr_i][curr_j] = 2
                    break
            sand += 1
            if out:
                print_maze(maze)
        except:
            keep_pouring = False

    return sand


def problem_2(out=False):
    walls_list, nrows, ncols, pouring = read_input()

    # Adjusting map
    new_nrows = nrows + 2
    new_ncols = 2 * new_nrows + 1
    new_pouring = new_ncols // 2 + 1
    displacement = new_pouring - pouring
    walls_list = [[(i, j + displacement) for (i, j) in pairs] for pairs in walls_list]
    walls_list.append([(new_nrows, 0), (new_nrows, new_ncols)])

    maze = create_maze(walls_list, new_nrows, new_ncols)
    sand = 0
    while True:
        if maze[0][new_pouring] == 2:
            break
        curr_i, curr_j = 0, new_pouring
        while True:
            if maze[curr_i+1][curr_j] == 0:
                curr_i += 1
            elif maze[curr_i + 1][curr_j - 1] == 0:
                curr_i, curr_j = curr_i + 1, curr_j - 1
            elif maze[curr_i + 1][curr_j + 1] == 0:
                curr_i, curr_j = curr_i + 1, curr_j + 1
            else:
                maze[curr_i][curr_j] = 2
                break
        sand += 1
        if out:
            print_maze(maze)

    return sand


if __name__ == '__main__':
    print(problem_1())
    print(problem_2())
