def main(raw_input):
    vals = [int(x) for x in raw_input.splitlines()]

    for i in vals:
        for j in vals:
            if i + j == 2020:
                return i * j

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
