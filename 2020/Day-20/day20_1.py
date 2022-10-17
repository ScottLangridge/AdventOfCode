from collections import defaultdict


class Tile:
    def __init__(self, input_string):
        input_string = input_string.strip('\n')
        input_rows = input_string.split('\n')

        self.id = int(input_rows.pop(0)[:-1].split(' ')[1])

        self.image = []
        for i in input_rows:
            self.image.append(list(i))

        self.borders = []
        self.borders.append(self.image[0])
        self.borders.append(self.image[-1])
        self.borders.append([row[0] for row in self.image])
        self.borders.append([row[-1] for row in self.image])
        self.borders.extend([list(reversed(border)) for border in self.borders])


def main(raw_input):
    # Parse input
    tiles = parse_input(raw_input)

    # Generate list of matching tiles
    matches = defaultdict(list)
    for t1 in range(len(tiles)):
        for t2 in range(t1 + 1, len(tiles)):
            for border in tiles[t1].borders:
                if border in tiles[t2].borders:
                    matches[tiles[t1].id].append(tiles[t2].id)
                    matches[tiles[t2].id].append(tiles[t1].id)
                    break

    # Identify corners and multiply ids
    out = 1
    for k, v in matches.items():
        if len(v) == 2:
            out *= k

    # Return solution
    return out


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    tile_strings = raw_input.split('\n\n')
    tiles = [Tile(i) for i in tile_strings]
    return tiles


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
