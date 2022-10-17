def main(raw_input):
    steps = [(line.split()[0], int(line.split()[1])) for line in raw_input.splitlines()]
    aim_delta = {
        'up': -1,
        'down': 1
    }

    aim = 0
    x, y = 0, 0
    for step in steps:
        action, dist = step
        if action == 'forward':
            x += dist
            y += aim * dist
        else:
            aim += aim_delta[action] * dist

    return x * y


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
