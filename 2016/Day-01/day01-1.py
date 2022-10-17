def main(raw_input):
    steps = raw_input.split(', ')

    dir_index = 0
    dirs = [
        [0, 1],  # N
        [1, 0],  # E
        [0, -1],  # S
        [-1, 0]  # W
    ]

    coords = [0, 0]
    for step in steps:
        if step.startswith('R'):
            dir_index = (dir_index + 1) % 4
        else:
            dir_index = (dir_index - 1) % 4

        coords[0] = coords[0] + (dirs[dir_index][0] * int(step[1:]))
        coords[1] = coords[1] + (dirs[dir_index][1] * int(step[1:]))

    return abs(coords[0]) + abs(coords[1])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
