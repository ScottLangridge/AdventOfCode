def main(raw_input):

    checksums = raw_input.split('\n')
    diffs = []

    for i in range(len(checksums)):
        checksum = list(map(lambda x: int(x), checksums[i].split('\t')))
        diffs.append(max(checksum) - min(checksum))

    return sum(diffs)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
