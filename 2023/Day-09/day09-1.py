class Sequence:
    def __init__(self, values):
        self.values = values
        self.is_terminal_sequence = values == [0] * len(values)
        if not self.is_terminal_sequence:
            self.sub_sequence = Sequence(self._generate_subsequence())

    def _generate_subsequence(self):
        diffs = []
        for i in range(len(self.values) - 1):
            diffs.append(self.values[i + 1] - self.values[i])
        return diffs

    def extrapolate(self):
        if self.is_terminal_sequence:
            return 0
        else:
            return self.values[-1] + self.sub_sequence.extrapolate()

    def print(self, indent):
        str_out = ','.join(['' for _ in range(indent)])
        str_out += ','.join([str(i) for i in self.values])
        print(str_out)

        if self.is_terminal_sequence:
            print()
        else:
            self.sub_sequence.print(indent + 1)


def debug(raw_input):
    sequences = raw_input.splitlines()
    for i, sequence in enumerate(sequences):
        sequences[i] = Sequence([int(i) for i in sequence.split()][:-1])
        if sequences[i].extrapolate() != [int(i) for i in sequence.split()][-1]:
            print(f'Failed on i={i}\nFull Sequence: {sequence}\nMy Sequence: {sequences[i].values}\nMy Next Val: {sequences[i].extrapolate()}, Real Next Val: {[int(i) for i in sequence.split()][-1]}')
            sequences[i].print(0)


def main(raw_input):
    sequences = raw_input.splitlines()
    for i, sequence in enumerate(sequences):
        sequences[i] = Sequence([int(i) for i in sequence.split()])

    return sum([seq.extrapolate() for seq in sequences])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
