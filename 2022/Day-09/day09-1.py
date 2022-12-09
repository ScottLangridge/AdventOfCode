class Move:
    def __init__(self, line):
        self.x, self.y, self.num = map(int, line.split())


def main(raw_input):
    raw_input = raw_input.replace('R', '1 0').replace('L', '-1 0').replace('U', '0 1').replace('D', '0 -1')
    moves = [Move(line) for line in raw_input.splitlines()]

    hx, hy, tx, ty = 0, 0, 0, 0
    tail_visited = set()
    for i in moves:
        for _ in range(i.num):
            hx += i.x
            hy += i.y
            tx, ty = update_tail(hx, hy, tx, ty)
            tail_visited.add((tx, ty))

    return len(tail_visited)


def update_tail(hx, hy, tx, ty):
    if hx - tx > 1:
        return hx - 1, hy
    elif hx - tx < -1:
        return hx + 1, hy
    elif hy - ty > 1:
        return hx, hy - 1
    elif hy - ty < -1:
        return hx, hy + 1
    else:
        return tx, ty


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
