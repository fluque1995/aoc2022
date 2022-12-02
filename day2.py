# Parse list of games to a list of pairs
def read_input():
    with open("inputs/day2.txt", "r") as fin:
        return [l.strip().split() for l in fin]


# Aux function: given a game, get the score
def get_score(game):
    WINS = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]
    DRAWS = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]
    score = 0
    # Score depending on win or draw (losing gives you no points)
    if game in WINS:
        score += 6
    elif game in DRAWS:
        score += 3

    # Score depending on your output (1 for rock, 2 for scissors, 3 for paper)
    if game[1] == 'X':
        score += 1
    elif game[1] == 'Y':
        score += 2
    elif game[1] == 'Z':
        score += 3

    return score


# Auxiliar function: given opponent move and game result, obtain your move
def get_move(game):
    if game in [['A', 'X'], ['B', 'Z'], ['C', 'Y']]:
        return 'Z'
    elif game in [['A', 'Y'], ['B', 'X'], ['C', 'Z']]:
        return 'X'
    elif game in [['A', 'Z'], ['B', 'Y'], ['C', 'X']]:
        return 'Y'


# PROBLEM 1: Score of games, assuming second column is your choice
def problem_1():
    matches = read_input()
    score = 0

    for game in matches:
        score += get_score(game)

    return score


# PROBLEM 2: Score of games, assuming second column is result of the game
def problem_2():
    matches = read_input()
    score = 0

    for game in matches:
        score += get_score([game[0], get_move(game)])

    return score


if __name__ == '__main__':
    print(problem_1())
    print(problem_2())
