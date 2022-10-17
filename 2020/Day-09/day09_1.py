def main(raw_input):
    window_size = 25

    xmas_data = parse_input(raw_input)

    i = window_size
    while i < len(xmas_data):
        if not index_is_valid(xmas_data, i, window_size):
            return xmas_data[i]
        i += 1

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [int(i) for i in raw_input.splitlines()]


def index_is_valid(xmas_data, index, window_size):
    window_vals = xmas_data[index - window_size:index]
    for num1 in window_vals:
        for num2 in window_vals:
            if num1 + num2 == xmas_data[index] and num1 != num2:
                return True

    return False


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
