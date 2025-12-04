def main(raw_input):
    grid = [list(line) for line in raw_input.splitlines()]

    accessible_count = 0
    last_accessible_count = -1
    while last_accessible_count != accessible_count:
        last_accessible_count = accessible_count

        accessible_list = []
        y = 0
        while y < len(grid):
            x = 0
            while x < len(grid[y]):
                if grid[y][x] == "@":
                    if accessible(grid, x, y):
                        accessible_list.append((y, x))
                        accessible_count += 1
                x += 1
            y += 1

        for y, x in accessible_list:
            grid[y][x] = "x"

    return accessible_count


def accessible(grid, x, y):
    min_x = 0
    max_x = len(grid[0]) - 1
    min_y = 0
    max_y = len(grid) - 1

    adjacent_count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            xdx = x + dx
            ydy = y + dy

            if dx == 0 and dy == 0:
                continue
            if not min_y <= ydy <= max_y:
                continue
            if not min_x <= xdx <= max_x:
                continue
            if grid[ydy][xdx] == "@":
                adjacent_count += 1

    return adjacent_count < 4


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
