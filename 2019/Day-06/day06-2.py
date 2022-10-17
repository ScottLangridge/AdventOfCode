from collections import defaultdict


def main(raw_input):
    data = parse_input(raw_input)

    # Map orbits
    parent = {}
    for (v, k) in data:
        parent[k] = v

    # Find first common node with santa
    current = parent['YOU']
    you_path = []
    while current != 'COM':
        you_path.append(current)
        current = parent[current]

    current = parent['SAN']
    san_path = []
    while current != 'COM':
        san_path.append(current)
        current = parent[current]

    for i in you_path:
        if i in san_path:
            return you_path.index(i) + san_path.index(i)


def lst_children(orbits, k):
    children = orbits[k]
    for i in orbits[k]:
        for child in lst_children(orbits, i):
            if child not in children:
                children.append(child)
    return children


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [line.split(')') for line in raw_input.splitlines()]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
