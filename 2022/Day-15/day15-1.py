from tqdm import tqdm


class Sensor:
    def __init__(self, line):
        split_line = line.split()
        self.x = int(split_line[2].strip('x=,'))
        self.y = int(split_line[3].strip('y=:'))
        self.bx = int(split_line[8].strip('x=,'))
        self.by = int(split_line[9].strip('y=:'))
        self.range = self.range_to(self.bx, self.by)

    def covers_point(self, x, y):
        return self.range_to(x, y) <= self.range

    def range_to(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def __str__(self):
        return f'S: ({self.x}, {self.y}), B: ({self.bx, self.by}), R: {self.range}'


def main(raw_input):
    sensors = [Sensor(line) for line in raw_input.strip().splitlines()]
    beacon_positions = set(map(lambda s: (s.bx, s.by), sensors))
    y = 2000000

    min_x = min(map(lambda s: s.x - s.range, sensors)) - 1
    max_x = max(map(lambda s: s.x + s.range, sensors)) + 1

    beaconless_points = 0
    for x in tqdm(range(min_x, max_x + 1)):
        if (x, y) in beacon_positions:
            continue

        for s in sensors:
            if s.covers_point(x, y):
                beaconless_points += 1
                break

    return beaconless_points


def parse_line(line):
    split_line = line.split()
    sx = int(split_line[2].strip('x=,'))
    sy = int(split_line[3].strip('y=:'))
    bx = int(split_line[8].strip('x=,'))
    by = int(split_line[9].strip('y=:'))
    return (sx, sy), (bx, by)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
