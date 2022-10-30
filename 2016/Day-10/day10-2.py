from collections import defaultdict


class Output:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def to_str(self):
        return f'{self.name}: {self.inventory}'

    def ready(self):
        return False

    def compares(self):
        return None


class Bot:
    def __init__(self):
        self.name = ""
        self.inventory = []
        self.lo = None
        self.hi = None
        self.compares = None

    def to_str(self):
        return f'{self.name}: {self.lo} | {self.hi}, {self.inventory}'

    def load_instruction(self, instruction):
        self.name = bot_name(instruction)
        if instruction.startswith("value "):
            self.inventory.append(int(instruction.split()[1]))
        else:
            self.lo = ' '.join(instruction.split()[5:7])
            self.hi = ' '.join(instruction.split()[10:])

    def ready(self):
        return len(self.inventory) == 2

    def operate(self, bots):
        self.inventory = sorted(self.inventory)
        self.compares = self.inventory[:]
        bots[self.lo].inventory.append(self.inventory.pop(0))
        bots[self.hi].inventory.append(self.inventory.pop(0))
        bots[self.name] = self


def main(raw_input):
    instructions = raw_input.strip().splitlines()
    bots = initialise_bots(instructions)
    bots = bots | initialise_outputs(bots)

    continue_loop = True
    while continue_loop:
        continue_loop = False
        for bot in bots:
            bot = bots[bot]
            if bot.ready():
                bot.operate(bots)
                continue_loop = True

    return bots["output 0"].inventory[0] * bots["output 1"].inventory[0] * bots["output 2"].inventory[0]


def initialise_bots(instructions):
    bot_hash = defaultdict(Bot)
    for i in instructions:
        bot_hash[bot_name(i)].load_instruction(i)
    return bot_hash


def initialise_outputs(bots):
    output_hash = {}
    for bot in bots.values():
        if bot.lo.startswith("output"):
            output_hash[bot.lo] = Output(bot.lo)
        if bot.hi.startswith("output"):
            output_hash[bot.hi] = Output(bot.hi)
    return output_hash


def bot_name(instruction):
    if instruction.startswith("value "):
        return " ".join(instruction.split()[4:])
    else:
        return " ".join(instruction.split()[:2])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
