class Instruction:
    def __init__(self, instruction_string):
        split_instruction = instruction_string.split()
        self.move_num = int(split_instruction[1])
        self.move_from = int(split_instruction[3]) - 1
        self.move_to = int(split_instruction[5]) - 1


def main(raw_input):
    stacks, instructions = raw_input.split('\n\n')
    stacks = parse_stacks(stacks)
    instructions = [Instruction(i) for i in instructions.splitlines()]

    for i in instructions:
        stacks[i.move_to].extend(pop_n(stacks[i.move_from], i.move_num))

    return ''.join(map(lambda i: i[-1], stacks))


def pop_n(lst, n):
    out = reversed(lst[-n:])
    del lst[-n:]
    return out


def parse_stacks(str_stacks):
    stacks = [i.strip(' []').split(',') for i in ('\n' + str_stacks).replace('\n', '\n ').replace('    ', ' [ ]').replace('] [', ',').splitlines()][1:-1]
    return [list(filter(lambda i: i != ' ' and i != '', reversed(stack))) for stack in zip(*stacks)]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('super_input.txt')
    print(main(puzzle_input))
