def main(raw_input):
    data = parse_input(raw_input)

    total_fuel = 0
    for module_mass in data:
        module_fuel = (int(module_mass) // 3) - 2
        total_fuel += module_fuel

    return str(total_fuel)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split('\n')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
