from itertools import permutations


class RISCy:
    def __init__(self, print_output=False, pause_on_output=False):
        # Registers
        self._pc = 0
        self._memory = []
        self._input_queue = []
        self._io_log = []

        # Configuration
        self._pause_on_output = pause_on_output
        self.print_output = print_output

        # Flags
        self._halt_flag = False
        self._pause_flag = False

        # Instructions
        self._instruction_set = {
            99: {'len': 1, 'function': self._halt},
            1: {'len': 4, 'function': self._add},
            2: {'len': 4, 'function': self._mult},
            3: {'len': 2, 'function': self._input},
            4: {'len': 2, 'function': self._output},
            5: {'len': 3, 'function': self._jump_if_true},
            6: {'len': 3, 'function': self._jump_if_false},
            7: {'len': 4, 'function': self._less_than},
            8: {'len': 4, 'function': self._equals}
        }

    def set_memory(self, data):
        self._memory = data

    def set_noun_verb(self, noun, verb):
        self._memory[1] = noun
        self._memory[2] = verb

    def set_input_queue(self, inputs):
        self._input_queue = inputs

    def queue_input(self, val):
        self._input_queue.append(val)

    def get_io_log(self):
        return self._io_log

    def halted(self):
        return self._halt_flag

    def reset_pause_flag(self):
        self._pause_flag = False

    def run(self):
        while not (self._halt_flag or self._pause_flag):
            opcode, addressing_modes = self._process_instruction(self._memory[self._pc])
            first_operand = self._pc + 1
            last_operand = self._pc + self._instruction_set[opcode]['len']
            raw_operands = self._memory[first_operand:last_operand]
            operands = list(zip(raw_operands, addressing_modes))

            self._instruction_set[opcode]['function'](operands)
            self._pc += self._instruction_set[opcode]['len']

        return self._memory[0]

    def _process_instruction(self, instruction):
        instruction = str(instruction).zfill(2)
        opcode = int(instruction[-2:])

        instruction = instruction.zfill(self._instruction_set[opcode]['len'] + 1)
        modes = list(instruction[-3::-1])
        return opcode, modes

    def _eval_operand(self, operand):
        if operand[1] == '0':
            return self._memory[operand[0]]
        elif operand[1] == '1':
            return operand[0]

    def _add(self, operands):
        self._memory[operands[-1][0]] = self._eval_operand(operands[0]) + self._eval_operand(operands[1])

    def _mult(self, operands):
        self._memory[operands[-1][0]] = self._eval_operand(operands[0]) * self._eval_operand(operands[1])

    def _input(self, operands):
        if self._input_queue:
            val = int(self._input_queue[0])
            del self._input_queue[0]
        else:
            val = int(input('Input: '))
        self._io_log.append(val)
        self._memory[operands[0][0]] = val

    def _output(self, operands):
        val = str(self._eval_operand(operands[0]))
        self._io_log.append(val)
        if self.print_output:
            print('Output: ' + val)
        if self._pause_on_output:
            self._pause_flag = True

    def _jump_if_true(self, operands):
        if self._eval_operand(operands[0]) != 0:
            self._pc = self._eval_operand(operands[1]) - self._instruction_set[5]['len']

    def _jump_if_false(self, operands):
        if self._eval_operand(operands[0]) == 0:
            self._pc = self._eval_operand(operands[1]) - self._instruction_set[6]['len']

    def _less_than(self, operands):
        val = int(self._eval_operand(operands[0]) < self._eval_operand(operands[1]))
        self._memory[operands[2][0]] = val

    def _equals(self, operands):
        val = int(self._eval_operand(operands[0]) == self._eval_operand(operands[1]))
        self._memory[operands[2][0]] = val

    def _halt(self, operands=None):
        self._halt_flag = True


def main(raw_input):
    data = [int(x) for x in parse_input(raw_input)]

    possible_phase_settings = permutations([0, 1, 2, 3, 4])

    outputs = {}
    for config in possible_phase_settings:
        amp_input = 0
        for phase in config:
            amp = RISCy()
            amp.set_memory(data)
            amp.set_input_queue([phase, amp_input])
            amp.run()
            amp_input = amp.get_io_log()[-1]
        outputs[config] = int(amp_input)

    return max(outputs.values())


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
