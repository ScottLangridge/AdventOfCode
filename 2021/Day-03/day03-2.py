import numpy as np
from scipy import stats


def main(raw_input):
    report = np.array([list(map(lambda x: x == '1', line)) for line in raw_input.splitlines()])

    o2_report = report.copy()
    co2_report = report.copy()

    while len(o2_report) > 1:
        # For each column index
        for i in range(len(report[0, :])):
            match_bit = mode(o2_report[:, i])
            o2_report = filter_array_to_matching(o2_report, i, match_bit)
            if len(o2_report) == 1:
                break

    while len(co2_report) > 1:
        # For each column index
        for i in range(len(report[0, :])):
            match_bit = not mode(co2_report[:, i])
            co2_report = filter_array_to_matching(co2_report, i, match_bit)
            if len(co2_report) == 1:
                break

    return bin_arr_to_int(o2_report[0]) * bin_arr_to_int(co2_report[0])


def mode(col):
    return sum(col) >= len(col) / 2


def filter_array_to_matching(array, column, bit_to_match):
    filter_arr = array[:, column] == bit_to_match
    return array[filter_arr]


def bin_arr_to_int(bin_arr):
    mapping_dict = {True: '1', False: '0'}
    str_arr = list(map(lambda x: mapping_dict[x], bin_arr))
    return int(''.join(str_arr), 2)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
