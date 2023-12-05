class RangeMap:
    def __init__(self, str_range_block):
        range_strs = str_range_block.splitlines()[1:]
        self.ranges = [RangePair(i) for i in range_strs]

    def map(self, i):
        out = max([r.map(i) for r in self.ranges])
        if out != -1:
            return out
        else:
            return i


class RangePair:
    def __init__(self, range_str):
        dest_range_start, source_range_start, range_size = [int(i) for i in range_str.split()]
        self.source = Range(source_range_start, range_size)
        self.dest = Range(dest_range_start, range_size)

    def map(self, i):
        if self.source.includes(i):
            return self.dest.first + (i - self.source.first)
        else:
            return -1


class Range:
    def __init__(self, start, size):
        self.first = start
        self.last = start + size - 1

    def includes(self, val):
        return self.first <= val <= self.last


def main(raw_input):
    split_input = raw_input.split('\n\n')
    seeds = [int(i) for i in split_input[0].strip('seeds: ').split()]
    seed_to_soil = RangeMap(split_input[1])
    soil_to_fertilizer = RangeMap(split_input[2])
    fertilizer_to_water = RangeMap(split_input[3])
    water_to_light = RangeMap(split_input[4])
    light_to_temperature = RangeMap(split_input[5])
    temperature_to_humidity = RangeMap(split_input[6])
    humidity_to_location = RangeMap(split_input[7])

    locations = []
    for seed in seeds:
        soil = seed_to_soil.map(seed)
        fertilizer = soil_to_fertilizer.map(soil)
        water = fertilizer_to_water.map(fertilizer)
        light = water_to_light.map(water)
        temp = light_to_temperature.map(light)
        humidity = temperature_to_humidity.map(temp)
        locations.append(humidity_to_location.map(humidity))

    return min(locations)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
