import builtins


def read_input():
    with open("inputs/day13.txt", "r") as fin:
        groups = fin.read().split("\n\n")
        pairs = list(map(lambda x: x.strip().split("\n"), groups))

    return [(eval(lhs), eval(rhs)) for lhs, rhs in pairs]


def compare(lhs, rhs):
    if len(lhs) == 0 and len(rhs) == 0:
        return 0
    elif len(lhs) == 0:
        return -1
    elif len(rhs) == 0:
        return 1

    lhead, *ltail = lhs
    rhead, *rtail = rhs

    match [type(lhead), type(rhead)]:
        case [builtins.int, builtins.int]:
            return -1 if lhead < rhead else 1 if lhead > rhead else compare(ltail, rtail)

        case [builtins.list, builtins.list]:
            return x if (x:=compare(lhead, rhead)) != 0 else compare(ltail, rtail)

        case [builtins.int, builtins.list]:
            return x if (x:=compare([lhead], rhead)) != 0 else compare(ltail, rtail)

        case [builtins.list, builtins.int]:
            return x if (x:=compare(lhead, [rhead])) != 0 else compare(ltail, rtail)


def problem_1():
    acc = 0
    inp = read_input()
    for i, pair in enumerate(inp, 1):
        if compare(*pair) == -1:
            acc += i

    return acc


def problem_2():
    inp = read_input()
    flatten_inp = []
    for pair in inp:
        flatten_inp.extend(pair)

    div1, ind1 = [[2]], 1
    div2, ind2 = [[6]], 2

    for elem in flatten_inp:
        if compare(elem, div1) == -1:
            ind1 += 1
        if compare(elem, div2) == -1:
            ind2 += 1

    return ind1*ind2


print(problem_1())
print(problem_2())
