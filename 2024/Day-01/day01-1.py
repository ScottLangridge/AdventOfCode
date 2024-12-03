def main(raw_input):
    pairs = [line.split() for line in raw_input.splitlines()]
    lists = [*zip(*pairs)]
    lists[0] = sorted([int(i) for i in lists[0]])
    lists[1] = sorted([int(i) for i in lists[1]])

    i = 0
    sum = 0
    while i < len(lists[0]):
        a = lists[0][i]
        b = lists[1][i]
        diff = max(a, b) - min(a, b)
        sum += diff
        i+= 1

    return sum


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
