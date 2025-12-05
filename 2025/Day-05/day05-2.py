def main(raw_input):
    ranges_block, ingredients_block = raw_input.split("\n\n")

    fresh_ranges = [[int(i) for i in ranges_block.splitlines()[0].split("-")]]

    for _range in ranges_block.splitlines():
        new_range = [int(i) for i in _range.split("-")]
        overlapping_indexes = []

        for index, seen_range in enumerate(fresh_ranges):
            if ranges_overlap(seen_range, new_range):
                new_range = merge_ranges(seen_range, new_range)
                overlapping_indexes.append(index)

        for index in overlapping_indexes[::-1]:
            del fresh_ranges[index]
        fresh_ranges.append(new_range)

    possible_fresh_ids = 0
    for r in fresh_ranges:
        possible_fresh_ids += (r[1] - r[0]) + 1

    return possible_fresh_ids


def ranges_overlap(r1, r2):
    return (r1[0] <= r2[0] <= r1[1]
            or r1[0] <= r2[1] <= r1[1]
            or r2[0] <= r1[0] <= r2[1]
            or r2[0] <= r1[1] <= r2[1])


def merge_ranges(r1, r2):
    assert ranges_overlap(r1, r2)
    return [min([r1[0], r2[0]]), max([r1[1], r2[1]])]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
