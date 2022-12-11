def read_input():
    with open("inputs/day11.txt", "r") as fin:
        return [monkey.split("\n") for monkey in fin.read().split("\n\n")]


class Monkey:
    def __init__(self, monkey_info):
        self.worries = [int(e) for e in monkey_info[1].split(":")[1].split(",")]
        self.op = lambda x, y: (x*y if monkey_info[2].split(" ")[-2] == '*' else x+y)
        val_str = monkey_info[2].split(" ")[-1]
        self.value = int(val_str) if val_str != 'old' else None
        self.test = int(monkey_info[3].split(" ")[-1])
        self.true_ind = int(monkey_info[4].split(" ")[-1])
        self.false_ind = int(monkey_info[5].split(" ")[-1])

        self.inspections = 0

    def update_worry(self, item):
        return self.op(item, self.value) if self.value else self.op(item, item)

    def add_item(self, item):
        self.worries.append(item)

    def throw_objects(self, modulo):
        targets = []
        for item in self.worries:
            self.inspections += 1
            new_item = self.update_worry(item)
            if modulo is None:
                new_item //= 3
            else:
                new_item %= modulo
            if new_item % self.test == 0:
                targets.append((new_item, self.true_ind))
            else:
                targets.append((new_item, self.false_ind))

        self.worries = []
        return targets


def problem_1():
    monkeys = [Monkey(monkey_str) for monkey_str in read_input()]
    for i in range(20):
        for monkey in monkeys:
            objects = monkey.throw_objects(None)
            for item, target in objects:
                monkeys[target].add_item(item)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()

    return inspections[-2] * inspections[-1]


def problem_2():
    monkeys = [Monkey(monkey_str) for monkey_str in read_input()]
    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.test
    for i in range(10000):
        for monkey in monkeys:
            objects = monkey.throw_objects(modulo)
            for item, target in objects:
                monkeys[target].add_item(item)

    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()

    return inspections[-2] * inspections[-1]


if __name__ == '__main__':
    print(problem_1())
    print(problem_2())
