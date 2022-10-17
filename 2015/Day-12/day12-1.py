import re


def main(raw_input):
    return sum([int(x) for x in re.findall(r'-?\d+', raw_input)])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
