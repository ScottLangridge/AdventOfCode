import time
from collections import defaultdict


def main():
    # print('Test 1:', solve([+1, -1]))
    # print('Test 2:', solve([+3, +3, +4, -2, -4]))
    # print('Test 3:', solve([-6, +3, +8, +5, -6]))
    # print('Test 4:', solve([+7, +7, -2, -7, -4]))
    print('\nSolution:', solve(get_input()))


def get_input():
    out = []
    with open('input.txt', 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(int(line.strip("\n")))
    return out


def solve(puzzle_input):
    current_sum = 0
    found_sums = defaultdict(lambda: 0)

    while True:
        for i in puzzle_input:
            current_sum += i
            found_sums[current_sum] += 1

            if found_sums[current_sum] == 2:
                return current_sum


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
