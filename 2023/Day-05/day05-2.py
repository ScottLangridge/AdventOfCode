class Mapper:
    def __init__(self, mapper_definition):
        self.mappings = []

        lines = mapper_definition.splitlines()
        for line in lines[1:]:
            dest_start, source_start, size = [int(i) for i in line.split()]
            source_range = Range(source_start, source_start + size - 1)
            dest_range = Range(dest_start, dest_start + size - 1)
            self.mappings.append(RangeMapping(source_range, dest_range))

    def map_ranges(self, ranges):
        i = 0
        while i < len(ranges):
            range_in = ranges[i]
            for mapping in self.mappings:
                if mapping.source.disjoint_with(range_in):
                    continue
                elif mapping.source.contains(range_in):
                    ranges[i] = Range(range_in.start + mapping.shift, range_in.end + mapping.shift)
                elif range_in.contains(mapping.source):
                    ranges[i] = mapping.dest
                    if range_in.start != mapping.source.start:
                        ranges.insert(i + 1, Range(range_in.start, mapping.source.start - 1))
                    if mapping.source.end != range_in.end:
                        ranges.insert(i + 1, Range(mapping.source.end + 1, range_in.end))
                    break
                elif range_in.start_intersects(mapping.source):
                    ranges[i] = Range(range_in.start + mapping.shift, mapping.source.end + mapping.shift)
                    ranges.insert(i + 1, Range(mapping.source.end + 1, range_in.end))
                    break
                elif range_in.end_intersects(mapping.source):
                    ranges[i] = Range(mapping.source.start + mapping.shift, range_in.end + mapping.shift)
                    ranges.insert(i + 1, Range(range_in.start, mapping.source.start - 1))
                    break
                else:
                    raise 'Should never get here'

            i += 1

        return ranges


class RangeMapping:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.shift = dest.start - source.start


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'{list(range(self.start, self.end + 1))}'

    def disjoint_with(self, other):
        if self.start <= other.start <= self.end:
            return False
        elif other.start <= self.start <= other.end:
            return False
        else:
            return True

    def contains(self, other):
        return self.start <= other.start <= other.end <= self.end

    def contained_by(self, other):
        return other.contains(self)

    def start_intersects(self, other):
        return other.start <= self.start <= other.end

    def end_intersects(self, other):
        return other.start <= self.end <= other.end


def main(raw_input):
    split_input = raw_input.split('\n\n')

    seeds_definition = split_input[0]
    mapper_definitions = split_input[1:]

    working_ranges = get_seed_ranges(seeds_definition)
    for mapper_definition in mapper_definitions:
        mapper = Mapper(mapper_definition)
        working_ranges = mapper.map_ranges(working_ranges)

    return min([i.start for i in working_ranges])


def get_seed_ranges(seeds_definition):
    split = [int(i) for i in seeds_definition.strip('seeds: ').split()]
    starts = split[0::2]
    sizes = split[1::2]

    ranges = []
    for i in range(len(starts)):
        ranges.append(Range(starts[i], starts[i] + sizes[i] - 1))
    return ranges


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
