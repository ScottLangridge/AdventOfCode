def main(raw_input):
    rucksacks = [parse_rucksack(i) for i in raw_input.splitlines()]

    prio_sum = 0
    for i in range(0, len(rucksacks), 3):
        shared_item = set.intersection(rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]).pop()
        prio_sum += priority(shared_item)

    return prio_sum


def parse_rucksack(str):
    return set(str)


def priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
