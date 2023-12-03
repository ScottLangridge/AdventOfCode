def main(raw_input):
    schematic = [list(i) for i in raw_input.splitlines()]

    gear_ratios = []
    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if schematic[y][x] == '*':
                adjacent_part_numbers = list(get_adjacent_part_numbers(schematic, x, y))
                if len(adjacent_part_numbers) == 2:
                    gear_ratios.append(adjacent_part_numbers[0] * adjacent_part_numbers[1])

    return sum(gear_ratios)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def get_adjacent_part_numbers(schematic, x, y):
    adjacent_part_numbers = set()
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            xdx = x + dx
            ydy = y + dy
            if 0 <= ydy < len(schematic) and 0 <= xdx < len(schematic[0]):
                if schematic[ydy][xdx].isnumeric():
                    adjacent_part_numbers.add(detect_number(schematic, xdx, ydy))

    return adjacent_part_numbers


def detect_number(schematic, first_x, y):
    str_num = ''

    x = first_x
    while x - 1 >= 0 and schematic[y][x - 1].isnumeric():
        x -= 1

    while x < len(schematic[0]) and schematic[y][x].isnumeric():
        str_num += schematic[y][x]
        x += 1

    return int(str_num)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
