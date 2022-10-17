def main(raw_input):
    checksums = raw_input.split('\n')
    diffs = []
    for i in range(len(checksums)):
        checksum = list(reversed(sorted(list(map(lambda x: int(x), checksums[i].split('\t'))))))
        for j in range(len(checksum)):
            for k in range(j + 1, len(checksum)):
                if checksum[j] / checksum[k] % 1 == 0:
                    diffs.append(checksum[j] / checksum[k])

    return sum(diffs)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
