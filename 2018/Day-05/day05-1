import time


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readline()

    for char in raw:
        out.append(char)

    return out


def solve(puzzle_input):
    pairs = {}
    for i in range(26):
        pairs[chr(ord('a') + i)] = chr(ord('a') + i).upper()
        pairs[chr(ord('a') + i).upper()] = chr(ord('a') + i)

    i = 0
    while i < len(puzzle_input) - 1:
        if puzzle_input[i + 1] == pairs[puzzle_input[i]]:
            del puzzle_input[i]
            del puzzle_input[i]
            if i > 0:
                i -= 1
        else:
            i += 1

    return len(puzzle_input)


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
