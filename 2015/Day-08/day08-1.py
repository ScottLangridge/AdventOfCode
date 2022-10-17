def main(raw_input):
    strings = raw_input.splitlines()

    chars_removed = 0
    for string in strings:
        chars_removed += 2
        i = 0
        while i < len(string) - 1:
            if string[i] == '\\':
                next_char = string[i + 1]
                if next_char == '\\' or next_char == '"':
                    chars_removed += 1
                    i += 1
                elif next_char == 'x':
                    chars_removed += 3
                    i += 3
            i += 1

    return chars_removed


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
