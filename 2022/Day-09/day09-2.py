class Move:
    def __init__(self, line):
        self.x, self.y, self.num = map(int, line.split())


class Knot:
    def __init__(self):
        self.x, self.y = 0, 0


def main(raw_input):
    raw_input = raw_input.replace('R', '1 0').replace('L', '-1 0').replace('U', '0 1').replace('D', '0 -1')
    moves = [Move(line) for line in raw_input.splitlines()]

    rope = []
    for _ in range(10):
        rope.append(Knot())

    tail_visited = set()
    for move in moves:
        for _ in range(move.num):
            rope[0].x += move.x
            rope[0].y += move.y
            for i in range(1, len(rope)):
                this, last = rope[i], rope[i - 1]
                this.x, this.y = update_tail(last.x, last.y, this.x, this.y)
            tail_visited.add((rope[-1].x, rope[-1].y))

    return len(tail_visited)


def update_tail(hx, hy, tx, ty):
    if hx - tx > 1 and hy - ty > 1:
        return hx - 1, hy - 1
    if hx - tx > 1 and hy - ty < -1:
        return hx - 1, hy + 1
    if hx - tx < -1 and hy - ty > 1:
        return hx + 1, hy - 1
    if hx - tx < -1 and hy - ty < -1:
        return hx + 1, hy + 1
    if hx - tx > 1:
        return hx - 1, hy
    elif hx - tx < -1:
        return hx + 1, hy
    if hy - ty > 1:
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
