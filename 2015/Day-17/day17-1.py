import itertools


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def main(raw_input):
    containers = [int(x) for x in raw_input.splitlines()]
    combs = []
    for n in range(len(containers)):
        combs.extend(itertools.combinations(containers, n))

    return len(list(filter(lambda x: sum(x) == 150, combs)))


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
