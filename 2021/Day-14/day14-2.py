from collections import defaultdict


class PairInsertion:
    def __init__(self, insertion_def):
        split_def = insertion_def.split(' -> ')
        self.left = split_def[0][0]
        self.right = split_def[0][1]
        self.inserted = split_def[1]

    def __str__(self):
        return f'{self.left}{self.right} -> {self.inserted}'

    def matches(self, first, second):
        return first == self.left and second == self.right


def main(raw_input):
    current_polymer, raw_insertions = raw_input.split('\n\n')
    current_polymer = list(current_polymer)
    final_char = current_polymer[-1]
    insertions = [PairInsertion(line) for line in raw_insertions.splitlines()]
    insertions = {(insertion.left, insertion.right): insertion for insertion in insertions}

    pair_counts = defaultdict(int)
    for i in range(1, len(current_polymer)):
        pair_counts[(current_polymer[i - 1], current_polymer[i])] += 1

    for _ in range(40):
        step(pair_counts, insertions)

    char_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        char_counts[pair[0]] += pair_counts[pair]
    char_counts[final_char] += 1

    return max(char_counts.values()) - min(char_counts.values())


def step(pair_counts, insertions):
    frozen_pair_counts = {k: v for k, v in pair_counts.items()}
    for pair in frozen_pair_counts.keys():
        inserted = insertions[pair].inserted
        pair_counts[(pair[0], inserted)] += frozen_pair_counts[pair]
        pair_counts[(inserted, pair[1])] += frozen_pair_counts[pair]
        pair_counts[pair] -= frozen_pair_counts[pair]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
