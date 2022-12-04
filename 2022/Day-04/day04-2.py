def main(raw_input):
    pairs = [parse_pair(i) for i in raw_input.splitlines()]

    count = 0
    for pair in pairs:
        if ranges_overlap(pair[0], pair[1]):
            count += 1

    return count


def ranges_overlap(a, b):
    return (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1]) or (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1])


def parse_pair(pair_str):
    elf_pair = [i.split('-') for i in pair_str.split(',')]
    return [[int(num) for num in num_pair] for num_pair in elf_pair]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
