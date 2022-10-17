class Octopus:
    flashes = 0

    def __init__(self, energy, x, y):
        self.energy = energy
        self.x, self.y = x, y

        self.neighbors = []
        self.flashed = False

    def set_neighbors(self, octopus_locations):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                adjacent_pos = (self.x + dx, self.y + dy)
                if adjacent_pos in octopus_locations.keys():
                    self.neighbors.append(octopus_locations[adjacent_pos])
        self.neighbors.remove(self)

    def attempt_flash(self):
        if self.energy >= 10 and not self.flashed:
            self.flashed = True
            Octopus.flashes += 1
            for octo in self.neighbors:
                octo.neighbor_flashed()

    def neighbor_flashed(self):
        self.energy += 1
        self.attempt_flash()

    def end_step(self):
        self.flashed = False
        if self.energy >= 10:
            self.energy = 0


def main(raw_input):
    octopus_locations = {}
    for y, row in enumerate(raw_input.splitlines()):
        for x, energy in enumerate(row):
            octopus_locations[(x, y)] = Octopus(int(energy), x, y)

    octopuses = octopus_locations.values()
    for octo in octopuses:
        octo.set_neighbors(octopus_locations)

    for _ in range(100):
        step(octopuses)

    return Octopus.flashes


def step(octopuses):
    # Steps are three phases:
    #  1: Increment energy
    for octo in octopuses:
        octo.energy += 1

    #  2: Attempt to flash
    for octo in octopuses:
        octo.attempt_flash()

    # 3: Reset energies/flashed flags
    for octo in octopuses:
        octo.end_step()


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
