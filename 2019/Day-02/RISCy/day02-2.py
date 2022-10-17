class RISCy:
    def __init__(self):
        # Registers
        self._pc = None
        self._memory = []

        # Flags
        self._halt_flag = None

        # Instructions
        self._instruction_set = {
            99: {'len': 4, 'function': self._halt},
            1: {'len': 4, 'function': self._add},
            2: {'len': 4, 'function': self._mult},
        }

    def set_memory(self, data):
        self._memory = data

    def set_noun_verb(self, noun, verb):
        self._memory[1] = noun
        self._memory[2] = verb

    def run(self):
        self._pc = 0
        self._halt_flag = False

        while not self._halt_flag:
            opcode = self._memory[self._pc]
            first_operand = self._pc + 1
            last_operand = self._pc + self._instruction_set[opcode]['len']
            operands = self._memory[first_operand:last_operand]
            self._instruction_set[opcode]['function'](operands)
            self._pc += self._instruction_set[opcode]['len']

        return self._memory[0]

    def _add(self, operands):
        self._memory[operands[-1]] = self._memory[operands[0]] + self._memory[operands[1]]

    def _mult(self, operands):
        self._memory[operands[-1]] = self._memory[operands[0]] * self._memory[operands[1]]

    def _halt(self, operands):
        self._halt_flag = True


def main(raw_input):
    riscy = RISCy()
    data = [int(x) for x in parse_input(raw_input)]

    for noun in range(100):
        for verb in range(100):
            riscy.set_memory(data[:])
            riscy.set_noun_verb(noun, verb)
            if riscy.run() == 19690720:
                return (100 * noun) + verb


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('../input.txt')
    print(main(puzzle_input))
