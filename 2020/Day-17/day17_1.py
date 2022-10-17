from collections import defaultdict


class PocketDimension:
    def __init__(self, initial_slice):
        self._matrix = defaultdict(lambda: '.')

        for y in range(len(initial_slice)):
            for x in range(len(initial_slice[0])):
                self._matrix[(x, y, 0)] = initial_slice[y][x]

    def exec_cycle(self):
        next_matrix = defaultdict(lambda: '.')

        cube_keys = list(self._matrix.keys())
        for cube in cube_keys:
            next_matrix[cube] = self.cycle_cube(cube)
        new_cube_keys = filter(lambda key: key not in cube_keys, list(self._matrix.keys()))
        for cube in new_cube_keys:
            next_matrix[cube] = self.cycle_cube(cube)

        self._matrix = next_matrix

    def cycle_cube(self, cube_key):
        x, y, z = cube_key
        cube_active = self._matrix[cube_key] == '#'

        active_count = -1 if cube_active else 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    if self._matrix[(x + dx, y + dy, z + dz)] == '#':
                        active_count += 1

        if cube_active:
            if not (active_count == 2 or active_count == 3):
                return '.'
            else:
                return '#'
        else:
            if active_count == 3:
                return '#'
            else:
                return '.'

    def count_active(self):
        return list(self._matrix.values()).count('#')


def main(raw_input):
    pocket_dimension = PocketDimension(parse_input(raw_input))

    for i in range(6):
        pocket_dimension.exec_cycle()

    return pocket_dimension.count_active()


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [list(line) for line in raw_input.splitlines()]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
