import hashlib


def main(raw_input):
    key = raw_input
    suffix = 0

    while not hashlib.md5((key + str(suffix)).encode('utf-8')).hexdigest().startswith('000000'):
        suffix += 1

    return suffix


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
