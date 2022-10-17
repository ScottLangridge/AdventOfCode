from collections import defaultdict
from tqdm import tqdm


def main(raw_input):
    instructions = raw_input.splitlines()
    light_array = defaultdict(int)

    for i in tqdm(instructions):
        run_command(i, light_array)

    return sum(light_array.values())


def run_command(str_command, light_array):
    split_command = str_command.split()

    action = split_command[1]
    if action not in ['on', 'off']:
        action = 'toggle'

    corner_1 = [int(coord) for coord in split_command[-3].split(',')]
    corner_2 = [int(coord) for coord in split_command[-1].split(',')]
    addresses = get_light_addresses(corner_1, corner_2)

    for light in addresses:
        change_state(action, light, light_array)


def get_light_addresses(corner_1, corner_2):
    min_x = min([corner_1[0], corner_2[0]])
    max_x = max([corner_1[0], corner_2[0]])
    min_y = min([corner_1[1], corner_2[1]])
    max_y = max([corner_1[1], corner_2[1]])

    addresses = []
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            addresses.append((x, y))
    return addresses


def change_state(action, address, light_array):
    if action == 'on':
        light_array[address] += 1
    elif action == 'off':
        if light_array[address] > 0:
            light_array[address] -= 1
    else:
        light_array[address] += 2


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
