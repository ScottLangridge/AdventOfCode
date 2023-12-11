from itertools import product

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
    'O': [],
}

INSIDE_OFFSETS = {
    "L": (1, -1),
    "J": (-1, -1),
    "7": (-1, 1),
    "F": (1, 1),
}

ANTI_VERTEX = {
    'L': '7',
    '7': 'L',
    'F': 'J',
    'J': 'F',
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

    def adjacent_positions(self):
        adjacent_positions = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not (dx == 0 and dy == 0):
                    adjacent_positions.append(Position(self.x + dx, self.y + dy))
        return adjacent_positions


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
    p1_route, p2_route = [p1], [p2]
    p1_next, p2_next = pipe_map.find_adjacent_pipes(p1, p1_last)[0], pipe_map.find_adjacent_pipes(p2, p2_last)[0]
    while p1_next not in seen_positions and p2_next not in seen_positions:
        seen_positions.add(p1)
        seen_positions.add(p2)
        p1_last, p2_last = p1, p2
        p1, p2 = p1_next, p2_next
        p1_route.append(p1)
        p2_route.append(p2)
        p1_next = pipe_map.find_adjacent_pipes(p1, p1_last)[0]
        p2_next = pipe_map.find_adjacent_pipes(p2, p2_last)[0]

    pipe_route = [start_pos] + p1_route + list(reversed(p2_route[:-1]))

    inner_route = get_inside_route(pipe_map, pipe_route)

    set_pipe_route = set(pipe_route)
    set_inner_route = set(inner_route)

    for y in range(pipe_map.len_y):
        ln = ""
        for x in range(pipe_map.len_x):
            pos = Position(x, y)
            if pos in set_inner_route:
                ln += '.'
            elif pos in set_pipe_route:
                ln += '#'
            else:
                ln += ' '
        print(ln)
    print()

    return 'This is a horrible hack to just get this day over and done with. Copy the map above into your editor of choice, find and replace ". " with ".." and count the "."s\nI hope to come back and tidy this up at some point for my own sanity.'


def get_inside_route(pipe_map, route):
    len_route = len(route)

    pos_at_i = lambda: route[i % len_route]
    pipe_at_i = lambda: pipe_map.at(pos_at_i())
    pos_at = lambda index: route[index % len_route]
    pipe_at = lambda index: pipe_map.at(pos_at(index))

    assert pipe_at(1) == '-' and pipe_at(
        -1) == '|', "Hardcoded this to assume S is effectively an anti-F because it's a pain in the arse."
    inside_offset = INSIDE_OFFSETS[ANTI_VERTEX['F']]
    outer_route_start = pos_at(0)
    inner_route_start = pos_at(0).translate(*inside_offset)
    inner_route = []
    if inner_route_start not in route:
        inner_route.append(inner_route_start)

    i = 1
    while not pos_at_i() == outer_route_start:
        if pipe_at_i() == '-':
            add_pos(route, inner_route, pos_at_i().translate(0, inside_offset[1]))
        elif pipe_at_i() == '|':
            add_pos(route, inner_route, pos_at_i().translate(inside_offset[0], 0))
        elif pipe_at_i() in "LJ7F":
            if short_route(pipe_map, pos_at_i(), pos_at(i - 1), inside_offset):
                inside_offset = INSIDE_OFFSETS[pipe_at_i()]
                add_pos(route, inner_route, pos_at_i().translate(*inside_offset))
            else:
                inside_offset = INSIDE_OFFSETS[ANTI_VERTEX[pipe_at_i()]]
                for outside_vertex_offset in product([0, inside_offset[0]], [0, inside_offset[1]]):
                    add_pos(route, inner_route, pos_at_i().translate(*outside_vertex_offset))
        elif pipe_at_i() == "S":
            add_pos(route, inner_route, pos_at_i().translate(*inside_offset))

        i += 1

    return inner_route


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def add_pos(route, inner_route, pos):
    if pos not in route and pos not in inner_route:
        inner_route.append(pos)


# Determine whether to:
#   I | O        O | I
#   I L -   or   O L -
#   I I I        O O O
def short_route(pipe_map, pos, prev_pos, prev_offset):
    if pipe_map.at(pos) == 'L' and prev_pos == pos.translate(1, 0):
        return prev_offset[1] == -1
    if pipe_map.at(pos) == 'L' and prev_pos == pos.translate(0, -1):
        return prev_offset[0] == 1
    if pipe_map.at(pos) == '7' and prev_pos == pos.translate(-1, 0):
        return prev_offset[1] == 1
    if pipe_map.at(pos) == '7' and prev_pos == pos.translate(0, 1):
        return prev_offset[0] == -1
    if pipe_map.at(pos) == 'J' and prev_pos == pos.translate(-1, 0):
        return prev_offset[1] == -1
    if pipe_map.at(pos) == 'J' and prev_pos == pos.translate(0, -1):
        return prev_offset[0] == -1
    if pipe_map.at(pos) == 'F' and prev_pos == pos.translate(1, 0):
        return prev_offset[1] == 1
    if pipe_map.at(pos) == 'F' and prev_pos == pos.translate(0, 1):
        return prev_offset[0] == 1


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
