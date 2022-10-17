import time


def main():
    # print('Test:', solve(get_input('example1.txt')),'\n')
    print('Solution:', solve(get_input()))


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    pairs = 0
    triples = 0

    for code in puzzle_input:
        code = sorted(code)

        if has_count(code, 2):
            pairs += 1
        if has_count(code, 3):
            triples += 1

    return pairs * triples


def has_count(code, target_count):
    current_char = ''
    current_count = 0

    for char in code:
        if current_char == char:
            current_count += 1
        else:
            if current_count == target_count:
                return True
            else:
                current_char = char
                current_count = 1

    if current_count == target_count:
        return True
    else:
        return False


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
