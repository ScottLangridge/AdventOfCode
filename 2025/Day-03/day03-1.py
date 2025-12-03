def main(raw_input):
    banks = [[int(batt) for batt in bank] for bank in raw_input.splitlines()]

    total = 0
    for bank in banks:
        tens = max(bank[:-1])
        tens_pos = bank.index(tens)
        unit = max(bank[tens_pos + 1:])
        total += 10 * (tens) + unit

    return total


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
