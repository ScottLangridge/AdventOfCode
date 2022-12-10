class Screen:
    def __init__(self):
        self.cycle = 1
        self.reg_x = 1
        self.signal_strength = 0

    def increment(self):
        if (self.cycle - 20) % 40 == 0:
            self.signal_strength += self.cycle * self.reg_x
        self.cycle += 1


def main(raw_input):
    instructions = raw_input.splitlines()
    screen = Screen()

    for i in instructions:
        if i.startswith("addx"):
            screen.increment()
            screen.increment()
            v = int(i.split()[1])
            screen.reg_x += v
        else:
            screen.increment()

    return screen.signal_strength


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
