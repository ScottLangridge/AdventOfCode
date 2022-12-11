class Monkey:
    exec_out = None

    def __init__(self, monkey_string):
        split = [i.strip().split(': ') for i in monkey_string.splitlines()]
        self.items = [int(i) for i in split[1][1].split(', ')]
        self.operation = lambda old: exec("Monkey.exec_out = " + split[2][1].split(' = ')[1])
        self.test = lambda worry_level: worry_level % int(split[3][1].split()[-1]) == 0
        self.if_true = int(split[4][1].split()[-1])
        self.if_false = int(split[5][1].split()[-1])
        self.inspections = 0

    def take_turn(self, monkeys):
        while self.items:
            item = self.items.pop(0)
            target_monkey, item = self.inspect_item(item)
            monkeys[target_monkey].items.append(item)

    def inspect_item(self, item):
        self.inspections += 1
        self.operation(item)
        item = Monkey.exec_out
        item //= 3
        if self.test(item):
            return self.if_true, item
        else:
            return self.if_false, item


def main(raw_input):
    monkeys = {}
    for i, monkey_string in enumerate(raw_input.split('\n\n')):
        monkeys[i] = Monkey(monkey_string)

    monkey_count = len(monkeys.keys())
    for _ in range(20):
        for monkey_num in range(monkey_count):
            monkeys[monkey_num].take_turn(monkeys)

    sorted_inspections = sorted(map(lambda m: m.inspections, monkeys.values()))
    return sorted_inspections[-1] * sorted_inspections[-2]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
