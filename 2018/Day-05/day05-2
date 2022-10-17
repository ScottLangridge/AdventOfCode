import time
from collections import defaultdict


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n\n')
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
    len_after_unit = {}
    pairs = {}
    original_input = puzzle_input[:]
    for i in range(26):
        len_after_unit[chr(ord('a') + i)] = None
        pairs[chr(ord('a') + i)] = chr(ord('a') + i).upper()
        pairs[chr(ord('a') + i).upper()] = chr(ord('a') + i)

    completed = 0
    for unit in len_after_unit.keys():
        print(str((completed / 25) * 100).split('.')[0] + '% complete')
        completed += 1
        puzzle_input = original_input[:]
        removed = True
        while removed:
            removed = False
            if unit.lower() in puzzle_input:
                puzzle_input.remove(unit.lower())
                removed = True
            if unit.upper() in puzzle_input:
                puzzle_input.remove(unit.upper())
                removed = True

        i = 0
        while i < len(puzzle_input) - 1:
            if puzzle_input[i + 1] == pairs[puzzle_input[i]]:
                del puzzle_input[i]
                del puzzle_input[i]
                if i > 0:
                    i -= 1
            else:
                i += 1

        len_after_unit[unit] = len(puzzle_input)

    print('')
    return str(min(len_after_unit.values()))


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
