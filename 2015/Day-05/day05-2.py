def main(raw_input):
    strings = raw_input.splitlines()

    nice_strings = 0
    for str in strings:
        if is_nice(str):
            nice_strings += 1

    return nice_strings


def is_nice(string):
    # It contains at least one double letter pair
    match_found = False
    # For each pair of chars up to the third to last possible pair
    for i in range(len(string) - 3):
        pair = string[i:i + 2]
        # If it's repeated in the rest of the string, mark a match as found
        for ii in range(i + 2, len(string)):
            if pair == string[ii:ii + 2]:
                match_found = True
                break
        if match_found:
            break

    if match_found == False:
        return False

    # And it contains at least one double char (separated by one), it's nice.
    for i in range(2, len(string)):
        if string[i] == string[i - 2]:
            return True

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
