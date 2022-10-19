from collections import Counter


def main(raw_input):
    columns = list(zip(*[list(i) for i in raw_input.strip('\n').split('\n')]))
    return "".join(map(get_most_common_char, columns))


def get_most_common_char(string):
    counts = Counter(string)
    return max(counts, key=counts.get)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
