def main(raw_input):
    passports = parse_input(raw_input)

    valid_count = 0
    for i in passports:
        if is_valid(i):
            valid_count += 1

    return valid_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    # Change passport delimiter to ',' and remove newlines
    raw_input = raw_input.replace('\n\n', ',')
    raw_input = raw_input.replace('\n', ' ')

    # Convert all passports to dictionaries and add them to a list
    passport_strings = raw_input.split(',')
    return [passport_string_to_dict(x) for x in passport_strings]


def passport_string_to_dict(passport_string):
    passport_dict = {}
    attributes = passport_string.split(' ')
    attributes = [x.split(':') for x in attributes]
    for key, val in attributes:
        passport_dict[key] = val

    return passport_dict


def is_valid(passport):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in required_keys:
        if i not in passport.keys():
            return False
    return True

if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
