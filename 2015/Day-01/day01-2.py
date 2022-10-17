def main(raw_input):
    floor = 0
    for i, char in enumerate(raw_input):
        if char == '(':
            floor += 1
        else:
            floor -= 1
            if floor < 0:
                return i + 1


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
