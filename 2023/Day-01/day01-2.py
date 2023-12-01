import re

NUM_STRING_PREFIXES = {
    "one": "1",
    "two": "2",
    "thr": "3",
    "fou": "4",
    "fiv": "5",
    "six": "6",
    "sev": "7",
    "eig": "8",
    "nin": "9"
}

NUM_STRING_REGEX = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine))')

def main(raw_input):
    lines = raw_input.splitlines()

    calib_vals = []
    for line in lines:
        numbers = get_numbers(line)
        calib_vals.append(int(numbers[0] + numbers[-1]))

    return sum(calib_vals)


def get_numbers(string):
    out = []

    for i, char in enumerate(string):
        if char.isnumeric():
            out.append([char, i])

    # Turns out regex doesn't support overlapping strings, hence the lookahead and janky string prefix matching
    for match in re.finditer(NUM_STRING_REGEX, string):
        out.append([NUM_STRING_PREFIXES[string[match.start():match.start() + 3]], match.start()])

    # Deal with cases where there is only one number in the string
    if len(out) == 1:
        out.append(out[0])

    out.sort(key=lambda x: x[1])
    return list(map(lambda x: x[0], out))


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
