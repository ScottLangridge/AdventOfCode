def main(raw_input):
    lines = raw_input.splitlines()

    calib_vals = []
    for line in lines:
        numbers = list(filter(lambda i: i.isnumeric(), line))
        calib_vals.append(int(numbers[0] + numbers[-1]))

    return sum(calib_vals)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
