def main(raw_input):
    signal = raw_input

    for i in range(4, len(signal)):
        if len(set(signal[i - 4:i])) == 4:
            return i


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
