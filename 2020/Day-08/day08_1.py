class GameConsole:
    def __init__(self, program):
        self.instructions = {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp
        }

        self.pc = 0
        self.acc = 0

        self.prog = program

    def exec(self):
        visited = []

        while self.pc < len(self.prog):
            if self.pc in visited:
                return False, self.acc
            visited.append(self.pc)

            operator, operand = self.prog[self.pc]
            self.instructions[operator](operand)
            self.pc += 1

        return True, self.acc

    def nop(self, operand):
        pass

    def acc(self, operand):
        self.acc += operand

    def jmp(self, operand):
        self.pc += operand - 1


def main(raw_input):
    input_program = parse_input(raw_input)
    game_console = GameConsole(input_program)
    result = game_console.exec()

    return result[1]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    instructions = [i.split(' ') for i in raw_input.splitlines()]
    return [[i[0], int(i[1])] for i in instructions]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
