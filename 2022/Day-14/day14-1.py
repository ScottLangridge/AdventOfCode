from collections import defaultdict
from itertools import product


def main(raw_input):
    grid = defaultdict(lambda: '.')
    for line in raw_input.strip().splitlines():
        for rock_coord in parse_line(line):
            grid[rock_coord] = '#'

    source = (500, 0)
    max_y = max(map(lambda i: i[1], grid.keys()))

    sand_count = 0
    while True:
        sand_pos = list(source)
        next_pos = next_sand_pos(grid, sand_pos)
        while next_pos != sand_pos and next_pos[1] <= max_y:
            sand_pos = next_pos
            next_pos = next_sand_pos(grid, sand_pos)

        if next_pos[1] >= max_y:
            return sand_count

        sand_count += 1
        grid[next_pos] = 'o'


def next_sand_pos(grid, sand_pos):
    if grid[sand_pos[0], sand_pos[1] + 1] == '.':
        return sand_pos[0], sand_pos[1] + 1
    elif grid[sand_pos[0] - 1, sand_pos[1] + 1] == '.':
        return sand_pos[0] - 1, sand_pos[1] + 1
    elif grid[sand_pos[0] + 1, sand_pos[1] + 1] == '.':
        return sand_pos[0] + 1, sand_pos[1] + 1
    else:
        return tuple(sand_pos)


def parse_line(line):
    waypoints = line.strip().split(' -> ')
    waypoints = [list(map(int, point.split(','))) for point in waypoints]

    all_coords = []
    for i in range(len(waypoints) - 1):
        x_range = list(inclusive_range(*sorted(map(lambda i: i[0], [waypoints[i], waypoints[i + 1]]))))
        y_range = list(inclusive_range(*sorted(map(lambda i: i[1], [waypoints[i], waypoints[i + 1]]))))

        all_coords.extend(product(x_range, y_range))

    return all_coords


def inclusive_range(start, stop):
    return range(start, stop + 1)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
