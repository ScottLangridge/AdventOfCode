from collections import defaultdict
from tqdm import tqdm


def main(raw_input):
    coords = defaultdict(int)
    for line in raw_input.splitlines():
        for k, v in line_def_to_coords_arr(line).items():
            coords[k] += v

    return len(list(filter(lambda x: x > 1, coords.values())))


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def line_def_to_coords_arr(line):
    tokens = line.split()
    start_x, start_y = [int(x) for x in tokens[0].split(',')]
    end_x, end_y = [int(x) for x in tokens[2].split(',')]

    coords = defaultdict(int)

    # If horizontal/vertical
    if start_x == end_x or start_y == end_y:

        # Ensure correct ordering
        start_x, end_x = sorted([start_x, end_x])
        start_y, end_y = sorted([start_y, end_y])

        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                coords[(x, y)] += 1

    # Else: diagonal
    else:
        step_x = 1 if start_x <= end_x else -1
        step_y = 1 if start_y <= end_y else -1
        line_length = abs(end_x - start_x)

        dx, dy = 0, 0
        while abs(dx) <= line_length:
            coords[(start_x + dx, start_y + dy)] += 1
            dx += step_x
            dy += step_y

    return coords


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
