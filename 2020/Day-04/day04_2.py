import re


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
    year_regex = re.compile(r'\d\d\d\d')
    hgt_regex = re.compile(r'\d+(cm|in)')
    hcl_regex = re.compile(r'#(\d|[a-f])(\d|[a-f])(\d|[a-f])(\d|[a-f])(\d|[a-f])(\d|[a-f])')

    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in required_keys:
        if i not in passport.keys():
            return False

    if not (re.match(year_regex, passport['byr']) and 1920 <= int(passport['byr']) <= 2002):
        return False

    if not (re.match(year_regex, passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020):
        return False

    if not (re.match(year_regex, passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030):
        return False

    if not re.match(hgt_regex, passport['hgt']):
        return False
    elif passport['hgt'].endswith('cm') and not 150 <= int(passport['hgt'][:-2]) <= 193:
        return False
    elif passport['hgt'].endswith('in') and not 59 <= int(passport['hgt'][:-2]) <= 76:
        return False

    if not re.match(hcl_regex, passport['hcl']):
        return False

    valid_ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not passport['ecl'] in valid_ecls:
        return False

    if not (passport['pid'].isnumeric() and len(passport['pid']) == 9):
        return False

    return True


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
