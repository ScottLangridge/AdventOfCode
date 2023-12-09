def main(raw_input):
    raw_instructions, raw_map = raw_input.split('\n\n')
    instructions = [int(i) for i in raw_instructions.replace('L', '0').replace('R', '1')]

    map = {}
    for i in raw_map.splitlines():
        start, left, right = i.replace(' = (', ',').replace(' ', '').replace(')', '').split(',')
        map[start] = (left, right)

    i = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        current_node = map[current_node][instructions[i % len(instructions)]]
        i += 1

    return i


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
