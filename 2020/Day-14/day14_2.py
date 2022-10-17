class Mask:
    def __init__(self, mask_string):
        self.mask_string = mask_string
        self.variable_bits = mask_string.count('X')
        self.submasks = None
        self.expand_floats()

    def expand_floats(self):
        self.submasks = []
        binary_format_string = f'{{0:0{self.variable_bits}b}}'
        dec_submask_keys = range(2 ** self.variable_bits)
        bin_submask_keys = [list(binary_format_string.format(i)) for i in dec_submask_keys]

        for submask_key in bin_submask_keys:
            submask = list(self.mask_string)
            for i in range(len(submask)):
                if submask[i] == 'X':
                    submask[i] = submask_key.pop(0)
            self.submasks.append(''.join(submask))

    def apply(self, value):
        bin_val = list('{0:036b}'.format(value))

        for mask in self.submasks:
            for i in range(len(mask)):
                if self.mask_string[i] == 'X':
                    bin_val[i] = mask[i]
                elif self.mask_string[i] == '1':
                    bin_val[i] = '1'

            yield int(''.join(bin_val), 2)


def main(raw_input):
    instructions = parse_input(raw_input)
    memory = {}
    mask = None

    for i in instructions:
        if isinstance(i, str):
            mask = Mask(i)
        else:
            target_addresses = mask.apply(i[0])
            for address in target_addresses:
                memory[address] = i[1]

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


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
