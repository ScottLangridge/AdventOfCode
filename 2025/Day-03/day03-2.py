def main(raw_input):
    banks = [[int(batt) for batt in bank] for bank in raw_input.splitlines()]

    total = 0
    for bank in banks:
        working_bank = bank[:]

        position = 12
        while position > 0:
            max_joltage, index = get_max(working_bank, position - 1)
            working_bank = working_bank[index + 1:]
            total += max_joltage * (10 ** (position - 1))
            position -= 1

    return total

def get_max(bank, min_trailing):
    if len(bank) == 1:
        return bank[0], 0

    usable_bank = None
    if min_trailing > 0:
        usable_bank = bank[:-min_trailing]
    else:
        usable_bank = bank

    max_joltage = max(usable_bank)
    index = usable_bank.index(max_joltage)
    return max_joltage, index

def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
