def main(raw_input):
    steps = [(line.split()[0], int(line.split()[1])) for line in raw_input.splitlines()]
    translations = {
        'forward': (1, 0),
        'up': (0, -1),
        'down': (0, 1)
    }

    x, y = 0, 0
    for step in steps:
        trans, dist = step
        x += translations[trans][0] * dist
        y += translations[trans][1] * dist

    return x * y


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
