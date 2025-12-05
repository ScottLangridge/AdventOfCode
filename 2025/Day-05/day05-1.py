def main(raw_input):
    fresh_ranges = []
    ingredients = []

    ranges_block, ingredients_block = raw_input.split("\n\n")
    for _range in ranges_block.splitlines():
        fresh_ranges.append([int(i) for i in _range.split("-")])
    ingredients = [int(i) for i in ingredients_block.splitlines()]

    fresh_count = 0
    for i in ingredients:
        for r in fresh_ranges:
            if r[0] <= i <= r[1]:
                fresh_count += 1
                break

    return fresh_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
