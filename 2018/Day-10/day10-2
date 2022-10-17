import time
from copy import deepcopy


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw[:-1]:
        line = line.replace(' ', '').replace('position=<', '').replace('velocity=<', ',').replace('>', '')
        line = line.split(',')

        pos = [int(line[0]), int(line[1])]
        vel = [int(line[2]), int(line[3])]
        out.append([pos, vel])
    return out


def solve(puzzle_input):
    curr = puzzle_input
    count = 0
    while True:
        prev = deepcopy(curr)
        curr = run_tick(curr)
        prev_size = get_size(prev)
        curr_size = get_size(curr)

        if curr_size[0] >= prev_size[0] and curr_size[1] >= prev_size[1]:
            return count
        count += 1


def get_size(stars):
    min_x = max_x = stars[0][0][0]
    min_y = max_y = stars[0][0][1]

    for star in stars[1:]:
        if star[0][0] < min_x:
            min_x = star[0][0]
        elif star[0][0] > max_x:
            max_x = star[0][0]
        if star[0][1] < min_y:
            min_y = star[0][1]
        elif star[0][1] > max_y:
            max_y = star[0][1]

    return [max_x - min_x, max_y - min_y]


def run_tick(stars):
    for i in range(len(stars)):
        for j in range(2):
            stars[i][0][j] += stars[i][1][j]

    return stars


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
