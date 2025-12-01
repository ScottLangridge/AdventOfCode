def main(raw_input):
    mult = {
        "L": -1,
        "R": 1
    }

    zero_count = 0

    dial = 50
    for line in raw_input.split('\n'):
        dir = line[0]
        dist = int(line[1:])
        for i in range(dist):
            dial = (dial + (1 * mult[dir])) % 100
            if dial == 0:
                zero_count += 1

    return zero_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
