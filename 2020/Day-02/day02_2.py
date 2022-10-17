def main(raw_input):
    records = [parse_record(x) for x in raw_input.splitlines()]

    invalid_count = 0
    for i in records:
        if is_valid(i):
            invalid_count += 1

    return invalid_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_record(record):
    policy, password = record.split(': ')
    indexes, char = policy.split(' ')
    indexes = [int(x) for x in indexes.split('-')]

    return {'indexes': indexes, 'char': char, 'pass': password}


def is_valid(record):
    char_count = 0
    for i in record['indexes']:
        if record['pass'][i - 1] == record['char']:
            char_count += 1

    return char_count == 1


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
