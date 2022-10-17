def main(raw_input):
    data = parse_input(raw_input)

    total_fuel = 0
    for module_mass in data:
        total_fuel += get_fuel_requirement(int(module_mass))

    return str(total_fuel)


def get_fuel_requirement(mass):
    required_fuel = (mass // 3) - 2
    if required_fuel > 0:
        return required_fuel + get_fuel_requirement(required_fuel)
    else:
        return 0


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split('\n')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
