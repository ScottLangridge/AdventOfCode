def main(raw_input):
    seqs = raw_input.strip('\n').split('\n')
    button_locations = {
        (0, 2): "1",
        (1, 2): "2",
        (2, 2): "3",
        (0, 1): "4",
        (1, 1): "5",
        (2, 1): "6",
        (0, 0): "7",
        (1, 0): "8",
        (2, 0): "9",
    }

    code = ""
    coords = [1, 1]
    for seq in seqs:
        coords = move_sequence(coords, seq)
        code += button_locations[tuple(coords)]

    return code


def move_sequence(coords, seq):
    for move in seq:
        coords = move_once(coords, move)

    return coords


def move_once(coords, d):
    dirs = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0],
    }
    return [max(0, min(2, coords[0] + dirs[d][0])), max(0, min(2, coords[1] + dirs[d][1]))]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
