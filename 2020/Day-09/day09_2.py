def main(raw_input):
    xmas_data = parse_input(raw_input)
    invalid_val = 105950735

    first = 0
    last = 0
    while sum(xmas_data[first:last]) != invalid_val:
        if sum(xmas_data[first:last]) < invalid_val:
            last += 1
        else:
            first += 1

    return min(xmas_data[first:last]) + max(xmas_data[first:last])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [int(i) for i in raw_input.splitlines()]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
