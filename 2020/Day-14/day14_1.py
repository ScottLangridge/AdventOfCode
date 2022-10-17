def main(raw_input):
    instructions = parse_input(raw_input)
    memory = {}
    mask = ''

    for i in instructions:
        if isinstance(i, str):
            mask = i
        else:
            memory[i[0]] = apply_mask(mask, i[1])

    return sum(memory.values())


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    instructions = raw_input.splitlines()
    for i in range(len(instructions)):
        if 'mem' in instructions[i]:
            address, value = instructions[i].split(' = ')
            address = address[4:-1]
            instructions[i] = [int(address), int(value)]
        else:
            instructions[i] = instructions[i][-36:]

    return instructions


def apply_mask(mask, dev_val):
    bin_val = list(dec_to_binary(dev_val))

    for i in range(len(mask)):
        if mask[i] != 'X':
            bin_val[i] = mask[i]
    return int(''.join(bin_val), 2)


def dec_to_binary(value):
    return '{0:036b}'.format(value)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
