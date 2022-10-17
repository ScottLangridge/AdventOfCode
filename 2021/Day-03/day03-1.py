import numpy as np
from scipy import stats


def main(raw_input):
    report = np.array([list(line) for line in raw_input.splitlines()])
    transposed_report = report.transpose()

    g, e = '', ''
    for col in transposed_report:
        mode = stats.mode(col).mode.item(0)
        if mode == '1':
            g += '1'
            e += '0'
        else:
            e += '1'
            g += '0'

    return int(g, 2) * int(e, 2)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
