COMPASS_POINTS = {
    'n': (0, -1),
    'e': (1, 0),
    's': (0, 1),
    'w': (-1, 0)
}

VALID_CONNECTIONS = {
    'S': ['n', 'e', 's', 'w'],
    '|': ['n', 's'],
    '-': ['e', 'w'],
    'L': ['n', 'e'],
    'J': ['n', 'w'],
    '7': ['s', 'w'],
    'F': ['e', 's'],
    '.': [],
}



class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(f'({self.x}, {self.y})')

    def translate(self, dx, dy):
        return Position(self.x + dx, self.y + dy)


class PipeMap:
    def __init__(self, puzzle_input):
        self.grid = [list(line) for line in puzzle_input.splitlines()]
        self.len_y = len(self.grid)
        self.len_x = len(self.grid[0])

    def at(self, pos):
        return self.grid[pos.y][pos.x]

    def pos_in_bounds(self, pos):
        return 0 <= pos.x <= self.len_x and 0 <= pos.y <= self.len_y

    def find_s(self):
        for y, row in enumerate(self.grid):
            for x, char in enumerate(row):
                if char == 'S':
                    return Position(x, y)
        assert False, 'S not found'

    def find_adjacent_pipes(self, pos, pos_last=Position(-1, -1)):
        pipe = self.at(pos)

        adjacent_pipe_positions = []
        valid_connections = VALID_CONNECTIONS[pipe]
        for connection in valid_connections:
            pos_next = pos.translate(*COMPASS_POINTS[connection])
            if self.pos_in_bounds(pos_next) and pos_next != pos_last:
                adjacent_pipe_positions.append(pos_next)

        return adjacent_pipe_positions


def main(raw_input):
    pipe_map = PipeMap(raw_input)
    start_pos = pipe_map.find_s()

    seen_positions = {start_pos}
    p1_last, p2_last = start_pos, start_pos
    p1, p2 = filter(lambda p: start_pos in pipe_map.find_adjacent_pipes(p), pipe_map.find_adjacent_pipes(start_pos))
    p1_next = pipe_map.find_adjacent_pipes(p1, p1_last)[0]
    p2_next = pipe_map.find_adjacent_pipes(p2, p2_last)[0]
    steps = 1
    while p1_next not in seen_positions and p2_next not in seen_positions:
        seen_positions.add(p1)
        seen_positions.add(p2)
        p1_last, p2_last = p1, p2
        p1, p2 = p1_next, p2_next
        p1_next = pipe_map.find_adjacent_pipes(p1, p1_last)[0]
        p2_next = pipe_map.find_adjacent_pipes(p2, p2_last)[0]
        steps += 1

    return steps


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
