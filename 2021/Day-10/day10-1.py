def main(raw_input):
    lines = raw_input.splitlines()
    return sum(syntax_error_score(i) for i in lines)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def syntax_error_score(line):
    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    closers = {')': '(', ']': '[', '}': '{', '>': '<'}
    openers = closers.values()

    char_stack = []
    for char in line:
        if char in openers:
            char_stack.append(char)
        else:
            if char_stack.pop() != closers[char]:
                return scores[char]

    return 0


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
