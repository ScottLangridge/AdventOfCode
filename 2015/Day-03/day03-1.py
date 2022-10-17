from collections import defaultdict


def main(raw_input):
    directions = raw_input
    steps = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }

    visits = defaultdict(int)
    pos = (0, 0)

    visits[pos] += 1
    for i in directions:
        step = steps[i]
        pos = (pos[0] + step[0], pos[1] + step[1])
        visits[pos] += 1

    return len(visits)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
