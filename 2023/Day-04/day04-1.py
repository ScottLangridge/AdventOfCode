def main(raw_input):
    cards = raw_input.splitlines()

    points = 0
    for card in cards:
        card_id, card_numbers = card.split(': ')
        winning_nums, elf_nums = map(lambda x: set(x.split()), card_numbers.replace('  ', ' ').split(' | '))
        matches = len(elf_nums.intersection(winning_nums))
        if matches:
            points += 1 * (2 ** (matches - 1))

    return points


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
