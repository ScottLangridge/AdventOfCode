from collections import defaultdict


def main(raw_input):
    directions = raw_input

    visits = defaultdict(int)
    s_pos = (0, 0)
    rs_pos = (0, 0)
    santas_turn = True

    visits[s_pos] += 1
    for i in directions:
        if santas_turn:
            s_pos = step(s_pos, i, visits)
        else:
            rs_pos = step(rs_pos, i, visits)
        santas_turn = not santas_turn

    return len(visits)


def step(pos, dir, visits):
    steps = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }

    step = steps[dir]
    pos = (pos[0] + step[0], pos[1] + step[1])
    visits[pos] += 1
    return pos


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
