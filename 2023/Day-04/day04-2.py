from collections import defaultdict

def main(raw_input):
    cards = raw_input.splitlines()
    ids = range(1, len(cards) + 1)
    copies = defaultdict(lambda: 1)
    for i in ids:
        copies[i]
        _, card_numbers = cards[i - 1].split(': ')
        winning_nums, elf_nums = map(lambda x: set(x.split()), card_numbers.replace('  ', ' ').split(' | '))
        matches = len(elf_nums.intersection(winning_nums))
        for n in range(matches):
            copies[i+n+1] += copies[i]

    return sum(copies.values())


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
