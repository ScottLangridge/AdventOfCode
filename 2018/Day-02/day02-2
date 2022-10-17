import time


def main():
    # solution = solve(get_input('example2.txt'), 0, len(get_input('example2.txt')))
    # print('Test:', get_matching(solution[0], solution[1]),'\n')
    solution = solve(get_input('input.txt'), 0, len(get_input('input.txt')))
    print('Solution:', get_matching(solution[0], solution[1]))


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input, checked, total):
    # print(checked, 'of', total)
    testing = puzzle_input[0]
    for code in puzzle_input[1:]:
        if codes_match(testing, code):
            return testing, code
    return solve(puzzle_input[1:], checked + 1, total)


def codes_match(code1, code2):
    differences = 0
    for i in range(len(code1)):
        if code1[i] != code2[i]:
            differences += 1
            if differences > 1:
                return False
    return True


def get_matching(code1, code2):
    out = ''
    for char in code1:
        if char in code2:
            out = out + char
    return out


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
