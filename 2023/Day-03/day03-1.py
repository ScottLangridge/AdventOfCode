def main(raw_input):
    schematic = [list(i) for i in raw_input.splitlines()]

    in_number = False
    numbers = []
    for y, row in enumerate(schematic):
        for x, char in enumerate(row):
            if char.isnumeric() and in_number is False:
                numbers.append(detect_number(schematic, x, y))
                in_number = True
            elif not char.isnumeric():
                in_number = False

    part_numbers = []
    for number in numbers:
        for x, y in number[1]:
            if neighbor_contains_symbol(schematic, x, y):
                part_numbers.append(number[0])
                break

    return sum(part_numbers)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def detect_number(schematic, first_x, y):
    str_num = ''

    x = first_x
    coords = []
    while x < len(schematic[0]) and schematic[y][x].isnumeric():
        str_num += schematic[y][x]
        coords.append((x, y))
        x += 1

    return int(str_num), coords


def neighbor_contains_symbol(schematic, x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if 0 <= y + dy < len(schematic) and 0 <= x + dx < len(schematic[0]):
                if schematic[y + dy][x + dx] not in '.1234567890':
                    return True
    return False


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
