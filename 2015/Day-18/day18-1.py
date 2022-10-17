from tqdm import tqdm


class Grid:
    def __init__(self, raw_input):
        self._grid = {}
        for y, row in enumerate(raw_input.splitlines()):
            for x, light in enumerate(row):
                self._grid[(x, y)] = light == '#'

    def total_lit(self):
        return sum(self._grid.values())

    def update_grid(self):
        new_grid = {}
        for pos in self._grid.keys():
            new_grid[pos] = self._next_state(pos)
        self._grid = new_grid

    def _next_state(self, pos):
        lit_neighbors = self._lit_neighbors(pos)
        if self.lit(pos):
            return lit_neighbors in [2, 3]
        else:
            return lit_neighbors == 3

    def _lit_neighbors(self, pos):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                neighbor_pos = (pos[0] + dx, pos[1] + dy)
                if self.lit(neighbor_pos):
                    count += 1

        # Don't count yourself
        if self.lit(pos):
            count -= 1

        return count

    def lit(self, pos):
        try:
            return self._grid[pos]
        except KeyError:
            return False


def main(raw_input):
    grid = Grid(raw_input)

    for _ in tqdm(range(100)):
        grid.update_grid()

    return grid.total_lit()


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
