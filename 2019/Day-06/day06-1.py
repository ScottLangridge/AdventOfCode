from collections import defaultdict


def main(raw_input):
    data = parse_input(raw_input)

    orbits = defaultdict(list)
    for (k, v) in data:
        orbits[k].append(v)
    orbits = dict(orbits)

    return count_orbits(orbits, 'COM', 0)


def count_orbits(orbits, k, count):
    if k not in orbits.keys():
        return count
    else:
        directs = orbits[k]
        return count + sum([count_orbits(orbits, i, count + 1) for i in directs])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [line.split(')') for line in raw_input.splitlines()]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
