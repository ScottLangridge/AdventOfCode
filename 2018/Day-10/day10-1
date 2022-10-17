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
    while True:
        prev = deepcopy(curr)
        curr = run_tick(curr)
        prev_size = get_size(prev)
        curr_size = get_size(curr)

        if curr_size[0] >= prev_size[0] and curr_size[1] >= prev_size[1]:
            print_sky(prev)
            return


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


def print_sky(stars):
    # Normalise start positions so that grid can start at (0,0)
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

    max_x += -min_x
    max_y += -min_y

    for i in range(len(stars)):
        stars[i][0][0] += -min_x
        stars[i][0][1] += -min_y

    # Generate list for sky image
    star_map = []
    for y in range(max_y + 1):
        star_map.append([])
        for x in range(max_x + 1):
            star_map[-1].append('.')

    count = 0
    for star in stars:
        star_map[star[0][1]][star[0][0]] = '#'
        count += 1

    # Draw sky
    out = ''
    for row in star_map:
        for val in row:
            out = out + val
        out = out + '\n'
    print(out)


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
