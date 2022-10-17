from collections import Counter


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
    insertions = [PairInsertion(line) for line in raw_insertions.splitlines()]
    insertions = {(insertion.left, insertion.right): insertion for insertion in insertions}

    for i in range(10):
        step(current_polymer, insertions)

    counts = Counter(current_polymer)
    return max(counts.values()) - min(counts.values())


def step(polymer, insertions):
    insertions_to_perform = []
    for i in range(1, len(polymer)):
        if (polymer[i - 1], polymer[i]) in insertions.keys():
            insertions_to_perform.append((i, insertions[(polymer[i - 1], polymer[i])]))

    while insertions_to_perform:
        insertion = insertions_to_perform.pop()
        polymer.insert(insertion[0], insertion[1].inserted)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
