def main(raw_input):
    instructions = [parse_instruction(i) for i in raw_input.strip().splitlines()]
    grid = [[' ' for _ in range(50)] for _ in range(6)]

    for i in instructions:
        grid = i[0](grid, i[1], i[2])

    return str_grid(grid)


def parse_instruction(instruction):
    split = instruction.split()
    if len(split) == 2:
        a, b = [int(i) for i in split[1].split('x')]
        op = rect
    elif split[1] == 'row':
        a = int(split[2].strip('y='))
        b = int(split[4])
        op = rot_row
    else:
        a = int(split[2].strip('x='))
        b = int(split[4])
        op = rot_col

    return op, a, b


def rect(grid, a, b):
    for y in range(b):
        for x in range(a):
            grid[y][x] = '#'
    return grid


def rot_row(grid, a, b):
    grid[a] = grid[a][-b:] + grid[a][:-b]
    return grid


def rot_col(grid, a, b):
    grid = rot_row(list(zip(*grid)), a, b)
    return [list(i) for i in list(zip(*grid))]


def str_grid(grid):
    out = '+' + '-' * 50 + '+\n'
    for row in grid:
        out += '|' + ''.join(row) + '|\n'
    out += '+' + '-' * 50 + '+\n'
    return out


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
