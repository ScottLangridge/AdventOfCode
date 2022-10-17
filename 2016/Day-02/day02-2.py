def main(raw_input):
    seqs = raw_input.strip('\n').split('\n')
    button_locations = [
        "xx1xx",
        "x234x",
        "56789",
        "xABCx",
        "xxDxx",
    ]

    code = ""
    coords = [0, 2]
    for seq in seqs:
        coords = move_sequence(coords, seq, button_locations)
        code += button_locations[coords[1]][coords[0]]

    return code


def move_sequence(coords, seq, button_locations):
    for move in seq:
        coords = move_once(coords, move, button_locations)

    return coords


def move_once(coords, d, button_locations):
    dirs = {
        "U": [0, -1],
        "D": [0, 1],
        "L": [-1, 0],
        "R": [1, 0],
    }

    new_x = max(0, min(4, coords[0] + dirs[d][0]))
    new_y = max(0, min(4, coords[1] + dirs[d][1]))

    if button_locations[new_y][new_x] == "x":
        return coords
    else:
        return [new_x, new_y]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
