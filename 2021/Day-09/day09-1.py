def main(raw_input):
    split_input = raw_input.splitlines()

    heightmap = {}
    for y, line in enumerate(split_input):
        for x, height in enumerate(line):
            heightmap[(x, y)] = int(height)

    max_y = len(split_input)
    max_x = len(split_input[0])

    risk_levels = []
    for y in range(max_y):
        for x in range(max_x):
            is_low, height = is_lowpoint(heightmap, (x, y))
            if is_low:
                risk_levels.append(height + 1)

    return sum(risk_levels)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def is_lowpoint(heightmap, pos):
    adjacent_positions = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
    adjacent_heights = [get_height(heightmap, i) for i in adjacent_positions]
    pos_height = get_height(heightmap, pos)
    return pos_height < min(adjacent_heights), pos_height


def get_height(heightmap, pos):
    try:
        return heightmap[pos]
    except KeyError:
        return 10


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
