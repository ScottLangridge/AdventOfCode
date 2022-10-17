def main(raw_input):
    lower, upper = parse_input(raw_input)

    count = 0
    for i in range(lower, upper + 1):
        if is_valid(i):
            count += 1

    return count


def is_valid(num):
    return never_decreases(num) and has_matching_adjacents(num)


def never_decreases(num):
    num = str(num)
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i + 1]):
            return False
    return True


def has_matching_adjacents(num):
    num = str(num)
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            return True
    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [int(i) for i in raw_input.split('-')]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
