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
    minmax_count, char = policy.split(' ')
    min_count, max_count = minmax_count.split('-')

    return {'min': int(min_count), 'max': int(max_count), 'char': char, 'pass': password}


def is_valid(record):
    char_occurences = record['pass'].count(record['char'])
    return record['min'] <= char_occurences <= record['max']


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
