def main(raw_input):
    split_input = raw_input.splitlines()

    heightmap = {}
    for y, line in enumerate(split_input):
        for x, height in enumerate(line):
            heightmap[(x, y)] = int(height)

    max_y = len(split_input)
    max_x = len(split_input[0])

    low_points = []
    for y in range(max_y):
        for x in range(max_x):
            is_low, height = is_lowpoint(heightmap, (x, y))
            if is_low:
                low_points.append((x, y))

    basins = [get_basin(heightmap, i) for i in low_points]
    basin_sizes = sorted([len(basin) for basin in basins])

    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


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


def get_basin(heightmap, lowpoint_pos):
    visited = []
    unvisited = [lowpoint_pos]
    while unvisited:
        # Pop location to visit next
        pos = unvisited.pop()

        # Add all it's neighbours with a height < 9 to unvisited
        adjacent_positions = [(pos[0] - 1, pos[1]), (pos[0] + 1, pos[1]), (pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
        for adjacent in adjacent_positions:
            if adjacent not in visited + unvisited and get_height(heightmap, adjacent) < 9:
                unvisited.append(adjacent)

        # Mark location as visited
        visited.append(pos)

    # Basin is the locations that were visited
    return visited


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
