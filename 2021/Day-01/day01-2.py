def main(raw_input):
    depths = [int(x) for x in raw_input.splitlines()]
    increases = 0
    for i in range(3, len(depths)):
        # Depths i - 1 and i - 2 are irrelevant since they're in both windows.
        if depths[i] > depths[i - 3]:
            increases += 1

    return increases


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
