from collections import Counter
from tqdm import tqdm


def main(raw_input):
    valid_combinations = 0

    for record in tqdm(raw_input.splitlines()):
        num_blanks = Counter(record)['?']
        for n in range(2 ** num_blanks):
            if valid_record(record, num_blanks, n):
                valid_combinations += 1

    return valid_combinations


def valid_record(record, num_blanks, n):
    fill_in_with = list(bin(n)[2:].zfill(num_blanks).replace('0', '.').replace('1', '#'))
    if Counter(fill_in_with)['#'] + Counter(record)['#'] != sum([int(i) for i in record.split()[1].split(',')]):
        return False

    continuous_brokens = []
    next_char = ""
    broken = 0
    for val in record.split()[0]:
        if val == '?':
            next_char = fill_in_with.pop(0)
        else:
            next_char = val

        if next_char == '#':
            broken += 1
        elif next_char == '.':
            if broken > 0:
                continuous_brokens.append(broken)
                broken = 0
    if broken > 0:
        continuous_brokens.append(broken)
        broken = 0

    return ','.join([str(i) for i in continuous_brokens]) == record.split()[1]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
