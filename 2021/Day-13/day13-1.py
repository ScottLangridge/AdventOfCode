class Dot:
    def __init__(self, input_line):
        split_input = input_line.split(',')
        self.x = int(split_input[0])
        self.y = int(split_input[1])

    def fold(self, fold):
        if fold.axis == 'y':
            if self.y > fold.pos:
                dist_from_fold = self.y - fold.pos
                self.y = fold.pos - dist_from_fold
        else:
            if self.x > fold.pos:
                dist_from_fold = self.x - fold.pos
                self.x = fold.pos - dist_from_fold


class Fold:
    def __init__(self, input_line):
        split_input = input_line.split()[-1].split('=')
        self.axis = split_input[0]
        self.pos = int(split_input[1])


def main(raw_input):
    dots, folds = raw_input.split('\n\n')
    dots = [Dot(dot_def) for dot_def in dots.splitlines()]
    folds = [Fold(fold_def) for fold_def in folds.splitlines()]

    do_fold(folds[0], dots)

    return count_visible(dots)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def do_fold(fold, dots):
    for dot in dots:
        dot.fold(fold)


def count_visible(dots):
    return len(set([(dot.x, dot.y) for dot in dots]))


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
