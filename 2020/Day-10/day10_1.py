def main(raw_input):
    adaptors = parse_input(raw_input)

    i = 1
    differences = [adaptors[0]]
    while i < len(adaptors):
        differences.append(adaptors[i] - adaptors[i - 1])
        i += 1
    differences.append(3)

    return differences.count(1) * differences.count(3)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return sorted([int(i) for i in raw_input.splitlines()])


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
