class Mapper:
    def __init__(self, mapper_definition):
        self.mappings = []

        # Parse the block of text defining this mapper into a list of range mappings
        lines = mapper_definition.splitlines()
        for line in lines[1:]:
            dest_start, source_start, size = [int(i) for i in line.split()]
            source_range = Range(source_start, source_start + size - 1)
            dest_range = Range(dest_start, dest_start + size - 1)
            self.mappings.append(RangeMapping(source_range, dest_range))

    # Apply the range mappings associated with this mapper in-place.
    #
    # Mapping in place dodges all sorts of trouble with the bits of ranges left
    #   over after mapping ranges not wholly contained within one another.
    def map_ranges(self, ranges):
        i = 0
        while i < len(ranges):
            range_in = ranges[i]
            for mapping in self.mappings:
                if mapping.source.disjoint_with(range_in):
                    continue
                elif mapping.source.contains(range_in):
                    # Replace the range with the new range it maps to.
                    ranges[i] = Range(range_in.start + mapping.shift, range_in.end + mapping.shift)
                elif range_in.contains(mapping.source):
                    # Replace the overlapping section of the range with the new range it maps to.
                    ranges[i] = mapping.dest

                    # Add back any range that sticks out before the mapping starts.
                    if range_in.start != mapping.source.start:
                        ranges.insert(i + 1, Range(range_in.start, mapping.source.start - 1))

                    # Add back any range that sticks out after the mapping ends .
                    if mapping.source.end != range_in.end:
                        ranges.insert(i + 1, Range(mapping.source.end + 1, range_in.end))
                    break
                elif range_in.start_intersects(mapping.source):
                    # Replace the overlapping section of the range with the new range it maps to.
                    ranges[i] = Range(range_in.start + mapping.shift, mapping.source.end + mapping.shift)

                    # Add back any range that sticks out before the mapping starts.
                    ranges.insert(i + 1, Range(mapping.source.end + 1, range_in.end))
                    break
                elif range_in.end_intersects(mapping.source):
                    # Replace the overlapping section of the range with the new range it maps to.
                    ranges[i] = Range(mapping.source.start + mapping.shift, range_in.end + mapping.shift)

                    # Add back any range that sticks out after the mapping ends .
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
        # Start and end are inclusive
        self.start = start
        self.end = end

    # Helpful for debugging
    def __str__(self):
        return f'{list(range(self.start, self.end + 1))}'

    # Quickly identify if two ranges never touch.
    # |---|
    #        |---|
    def disjoint_with(self, other):
        if self.start <= other.start <= self.end:
            return False
        elif other.start <= self.start <= other.end:
            return False
        else:
            return True

    # Check if this range entirely contains another.
    # |-------|
    #   |---|
    def contains(self, other):
        return self.start <= other.start <= other.end <= self.end

    # Check if another range entirely contains this one.
    #   |---|
    # |-------|
    def contained_by(self, other):
        return other.contains(self)

    # Check if this range begins within another.
    #    |-----|
    # |-----|
    def start_intersects(self, other):
        return other.start <= self.start <= other.end

    # Check if this range ends within another.
    # |-----|
    #    |-----|
    def end_intersects(self, other):
        return other.start <= self.end <= other.end


def main(raw_input):
    # Input parsing
    split_input = raw_input.split('\n\n')
    seeds_definition = split_input[0]
    mapper_definitions = split_input[1:]

    # Set up seeds as a list of ranges that they span.
    working_ranges = get_seed_ranges(seeds_definition)

    # For each mapper, apply the mapping in-place to the entire list of ranges.
    # This hides a LOT of complexity
    for mapper_definition in mapper_definitions:
        mapper = Mapper(mapper_definition)
        working_ranges = mapper.map_ranges(working_ranges)

    # Return the min range start, which by this point is the min location.
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
