def main(raw_input):
    lines = raw_input.splitlines()
    incomplete_lines = filter(lambda i: not corrupted(i), lines)
    autocomplete_scores = sorted([autocomplete_score(line) for line in incomplete_lines])
    median_index = len(autocomplete_scores) // 2
    return autocomplete_scores[median_index]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def corrupted(line):
    closers = {')': '(', ']': '[', '}': '{', '>': '<'}
    openers = closers.values()

    char_stack = []
    for char in line:
        if char in openers:
            char_stack.append(char)
        else:
            if char_stack.pop() != closers[char]:
                return True

    return False


def autocomplete_score(line):
    score_values = {')': 1, ']': 2, '}': 3, '>': 4}
    bracket_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    openers = bracket_pairs.keys()

    char_stack = []
    for char in line:
        if char in openers:
            char_stack.append(char)
        else:
            char_stack.pop()

    completion = []
    while char_stack:
        next_closer = bracket_pairs[char_stack.pop()]
        completion.append(next_closer)

    completion_score = 0
    for char in completion:
        completion_score *= 5
        completion_score += score_values[char]

    return completion_score


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
