from math import sqrt, ceil


class Direction:
    def __init__(self, tag, dx, dy, next_dir):
        self.tag = tag
        self.dx = dx
        self.dy = dy
        self.next_dir = next_dir
    
    def next_dir(self):
        return self.next_dir

    def step(self, x, y):
        return x + self.dx, y + self.dy


def main(raw_input):
    # Parse Input
    target = int(raw_input)

    # Get ring
    next_odd_sqrt = ceil(sqrt(target))
    if next_odd_sqrt % 2 == 0:
        next_odd_sqrt += 1
    ring = (next_odd_sqrt - 1) // 2

    # Get location relative to ring square
    directions = {
        'n': Direction('n', 0, -1, 'e'),
        'e': Direction('e', 1, 0, 's'),
        's': Direction('s', 0, 1, 'w'),
        'w': Direction('w', -1, 0, 'n')
    }

    current_dir = directions['w']
    steps_in_dir = 0
    
    x_diff = 0
    y_diff = 0
    
    current_num = next_odd_sqrt ** 2
    while current_num > target:
        current_num -= 1
        x_diff, y_diff = current_dir.step(x_diff, y_diff)
        steps_in_dir += 1
        if steps_in_dir == next_odd_sqrt - 1:
            current_dir = directions[current_dir.next_dir]
            steps_in_dir = 0

    manhatten = abs(ring + x_diff) + abs(ring + y_diff)

    # Return solution
    return manhatten


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
