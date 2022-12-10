class Screen:
    def __init__(self):
        self.cycle = 1
        self.reg_x = 1
        self.image = ""

    def increment(self):
        pixel_lit = abs(((self.cycle - 1) % 40) - self.reg_x) <= 1
        self.image += "#" if pixel_lit else "."

        if self.cycle % 40 == 0:
            self.image += "\n"

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

    return screen.image


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
