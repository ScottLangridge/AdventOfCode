from collections import defaultdict
from itertools import permutations, chain


def main(raw_input):
    split_input = [x.split(' | ') for x in raw_input.splitlines()]
    input_signal_sets = [x[0].split() for x in split_input]
    output_signal_sets = [x[1].split() for x in split_input]

    output_vals_sum = 0
    for i in range(len(input_signal_sets)):
        mapping = get_segment_mapping(input_signal_sets[i])
        output_digits = get_output_digits(mapping, output_signal_sets[i])
        output_val = int(''.join([str(x) for x in output_digits]))
        output_vals_sum += output_val

    return output_vals_sum


# Take a set of jumbled signals and return a dict converting it to the standard signals
def get_segment_mapping(signal_set):
    signals_by_length = defaultdict(list)
    for i in signal_set:
        signals_by_length[len(i)].append(i)

    mapping = {}

    # Use the 1 (two segments) to get a pool of possible c and f
    cf = set(signals_by_length[2][0])

    # Use the 7 (three segments) to get a confirmed a
    acf = set(signals_by_length[3][0])
    mapping['a'] = (acf - cf).pop()

    # Use the 4 (four segments)  to get a pool of possible b and d
    bd = set(signals_by_length[4][0]) - cf

    # Use what is missing from the 9, 6 and 0 (all six segments) to get a pool of c, d and e
    cde = set((set('abcdefg') - set(i)).pop() for i in signals_by_length[6])

    # Only signal in both that pool and the c/f pool confirms c
    mapping['c'] = cde.intersection(cf).pop()

    # Remaining signal in c/f pool confirms f
    mapping['f'] = (cf - set(mapping['c'])).pop()

    # Only signals which appear once in 2, 3 and 5 (all five segments) are b and e
    joined = ''.join(signals_by_length[5])
    be = set(filter(lambda x: joined.count(x) == 1, joined))

    # Only signal in both b/e and b/d confirms b
    mapping['b'] = (be.intersection(bd)).pop()

    # Remaining signal in b/d pool confirms d
    mapping['d'] = (bd - set(mapping['b'])).pop()

    # e/g is what's left
    eg = (set('abcdefg') - set(mapping.values()))

    # The only signal out of e/g which appears in all six segment digits confirms g
    joined = ''.join(signals_by_length[6])
    three_appearances = set(filter(lambda x: joined.count(x) == 3, joined))
    mapping['g'] = eg.intersection(three_appearances).pop()

    # Remaining signal in e/g pool confirms e
    mapping['e'] = (eg - set(mapping['g'])).pop()

    # Reverse mapping so it maps encoded -> actual rather than actual -> encoded
    mapping = dict((v, k) for k, v in mapping.items())

    return mapping


def get_output_digits(signal_mapping, output_signals):
    true_output_signals = []
    for signal in output_signals:
        true_output_signals.append(''.join(sorted([signal_mapping[char] for char in signal])))

    signal_to_digit = {
        'abcefg': 0,
        'cf': 1,
        'acdeg': 2,
        'acdfg': 3,
        'bcdf': 4,
        'abdfg': 5,
        'abdefg': 6,
        'acf': 7,
        'abcdefg': 8,
        'abcdfg': 9,
    }

    return [signal_to_digit[x] for x in true_output_signals]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
