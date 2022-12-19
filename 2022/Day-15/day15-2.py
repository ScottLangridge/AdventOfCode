from tqdm import tqdm


class Sensor:
    def __init__(self, line):
        split_line = line.split()
        self.x = int(split_line[2].strip('x=,'))
        self.y = int(split_line[3].strip('y=:'))
        self.bx = int(split_line[8].strip('x=,'))
        self.by = int(split_line[9].strip('y=:'))
        self.range = self.range_to(self.bx, self.by)

    def min_max_x(self):
        return self.x - self.range, self.x + self.range

    def min_max_x_at_y(self, y):
        min_max_x = self.min_max_x()
        dy = abs(self.y - y)
        y_adjusted_range = self.range - dy
        if y_adjusted_range > 0:
            return min_max_x[0] + dy, min_max_x[1] - dy
        else:
            return []

    def range_to(self, x, y):
        return abs(self.x - x) + abs(self.y - y)

    def __str__(self):
        return f'S: ({self.x}, {self.y}), B: ({self.bx, self.by}), R: {self.range}'


def main(raw_input):
    sensors = [Sensor(line) for line in raw_input.strip().splitlines()]
    range_cap = 4000000

    for y in tqdm(range(range_cap + 1)):
        beaconless_ranges = []
        for sensor in sensors:
            covered_range = sensor.min_max_x_at_y(y)
            if covered_range:
                covered_range = crop_range(covered_range, 0, range_cap)
                beaconless_ranges = add_beaconless_range(beaconless_ranges, covered_range)

        # The beacon could technically be at the edge of the allowable coordinate space, meaning there will only be one
        # range, but I've not implemented a check for this because it doesn't matter for my input.
        if len(beaconless_ranges) == 2:
            beaconless_ranges.sort(key=lambda r: r[0])
            x = beaconless_ranges[0][1] + 1
            return x * 4000000 + y
        elif len(beaconless_ranges) != 1:
            raise RuntimeError("Something's gone wrong")


def crop_range(range, start, end):
    return max(range[0], start), min(range[1], end)


def add_beaconless_range(beaconless_ranges, new_range):
    intersecting_ranges = [new_range]

    i = 0
    while i < len(beaconless_ranges):
        if ranges_intersect(new_range, beaconless_ranges[i]):
            intersecting_ranges.append(beaconless_ranges.pop(i))
        else:
            i += 1

    beaconless_ranges.append(
        (min(map(lambda r: r[0], intersecting_ranges)), max(map(lambda r: r[1], intersecting_ranges)))
    )

    return beaconless_ranges


def ranges_intersect(r1, r2):
    return (r1[0] - 1 <= r2[0] <= r1[1] + 1
            or r1[0] - 1 <= r2[1] <= r1[1] + 1
            or r2[0] - 1 <= r1[0] <= r2[1] + 1
            or r2[0] - 1 <= r1[1] <= r2[1] + 1)


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
