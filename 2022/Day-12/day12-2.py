from collections import defaultdict


class Node:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y

        if h == -14:
            self.h = 0
        elif h == -28:
            self.h = 26
        else:
            self.h = h

        self.links = set()

    def link_node(self, node):
        if node.h <= self.h + 1:
            self.links.add(node)


def main(raw_input):
    heightmap = [input_line_to_heightmap_row(line) for line in raw_input.splitlines()]

    starts, end, nodes = build_graph(heightmap)

    distance_to = defaultdict(lambda: None)
    for start in starts:
        distance_to[start] = 0

    fringe = set(starts)
    while distance_to[end] is None:
        current_node = min(fringe, key=lambda i: distance_to[i])
        fringe.remove(current_node)

        for link in current_node.links:
            if distance_to[link] is None or distance_to[link] > distance_to[current_node] + 1:
                distance_to[link] = distance_to[current_node] + 1
                fringe.add(link)

    return distance_to[end]


def build_graph(heightmap):
    starts = []
    end = None
    nodes = {}
    for y, row in enumerate(heightmap):
        for x, val in enumerate(row):
            node = get_node(heightmap, nodes, x, y)

            if heightmap[y][x] == -14 or heightmap[y][x] == 0:
                starts.append(node)
            elif heightmap[y][x] == -28:
                end = node

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if out_of_bounds(heightmap, x + dx, y + dy):
                    continue
                else:
                    adj = get_node(heightmap, nodes, x + dx, y + dy)
                    node.link_node(adj)

    return starts, end, nodes


def get_node(heightmap, nodes, x, y):
    if (x, y) not in nodes.keys():
        nodes[(x, y)] = Node(x, y, heightmap[y][x])
    return nodes[(x, y)]


def out_of_bounds(heightmap, x, y):
    return x < 0 or x >= len(heightmap[0]) or y < 0 or y >= len(heightmap)


def input_line_to_heightmap_row(line):
    return [ord(i) - 97 for i in line]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
