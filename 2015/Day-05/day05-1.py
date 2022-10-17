def main(raw_input):
    strings = raw_input.splitlines()

    nice_strings = 0
    for str in strings:
        if is_nice(str):
            nice_strings += 1

    return nice_strings

def is_nice(string):
    # If it contains no naughty strings
    naughty_substrings = ['ab', 'cd', 'pq', 'xy']
    for sub in naughty_substrings:
        if sub in string:
            return False

    # And it contains at least three vowels
    vowel_count = 0
    for vowel in 'aeiou':
        if vowel in string:
            vowel_count += string.count(vowel)
    if vowel_count < 3:
        return False

    # And it contains at least one double char, it's nice.
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            return True

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
