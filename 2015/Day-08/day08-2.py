def main(raw_input):
    strings = raw_input.splitlines()

    char_diff = 0
    for string in strings:
        char_diff += 2
        for char in string:
            if char == '\\' or char == '"':
                char_diff += 1

    return char_diff


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
