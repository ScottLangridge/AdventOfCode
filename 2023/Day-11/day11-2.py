from itertools import combinations


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Grid:
    def __init__(self, puzzle_input):
        self.grid = [list(line) for line in puzzle_input.splitlines()]
        self.len_y = len(self.grid)
        self.len_x = len(self.grid[0])
        self.empty_rows = []
        self.empty_cols = []

    def at(self, pos):
        return self.grid[pos.y][pos.x]

    def row_at(self, y):
        return self.grid[y]

    def col_at(self, x):
        return [row[x] for row in self.grid]

    def manhattan_dist(self, pos1, pos2):
        plain_dist = abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
        min_x, max_x = sorted((pos1.x, pos2.x))
        min_y, max_y = sorted((pos1.y, pos2.y))
        expanded_sections_crossed = (len(filter(lambda i: min_x < i < max_x, self.empty_cols))
                                     + len(filter(lambda i: min_y < i < max_y, self.empty_rows)))
        return (plain_dist - expanded_sections_crossed) + (1000000 * expanded_sections_crossed)

    def expand(self):
        for y in range(self.len_y):
            if set(self.row_at(y)) == {'.'}:
                self.empty_rows.append(y)
        for x in range(self.len_x):
            if set(self.col_at(x)) == {'.'}:
                self.empty_cols.append(x)

    def find_galaxies(self):
        galaxies = []
        for y in range(self.len_y):
            for x in range(self.len_x):
                if self.at(Pos(x, y)) == '#':
                    galaxies.append(Pos(x, y))
        return galaxies


def main(raw_input):
    star_map = Grid(raw_input)
    star_map.expand()
    galaxies = star_map.find_galaxies()
    galaxy_pairs = combinations(galaxies, 2)
    shortest_routes = [star_map.manhattan_dist(g1, g2) for g1, g2 in galaxy_pairs]

    return sum(shortest_routes)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
