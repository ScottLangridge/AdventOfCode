class Cave:
    def __init__(self, cave_id):
        self.id = cave_id
        self.is_large = cave_id.isupper()
        self.connections = []

    def __str__(self):
        return self.id


def main(raw_input):
    caves = {}
    for connection in raw_input.splitlines():
        cave1, cave2 = [get_cave(caves, x) for x in connection.split('-')]
        cave1.connections.append(cave2)
        cave2.connections.append(cave1)

    small_caves = list(filter(lambda x: not x.is_large, caves.values()))
    small_caves.remove(caves['start'])
    small_caves.remove(caves['end'])

    start, routes = caves['start'], []
    for small_cave in small_caves:
        routes.extend(get_routes(start, [start], small_cave))

    non_deadend_routes = list(filter(lambda x: x[-1].id == 'end', routes))
    unique_non_deadend_routes = set([tuple(x) for x in non_deadend_routes])

    return len(unique_non_deadend_routes)


def get_cave(caves, cave_id):
    if cave_id not in caves.keys():
        caves[cave_id] = Cave(cave_id)
    return caves[cave_id]


def get_routes(current, visited, visitable_twice):
    reachable = [cave for cave in current.connections if visitable(cave, visited, visitable_twice)]

    if not reachable or current.id == 'end':
        return [visited]

    routes = []
    for cave in reachable:
        next_visited = visited[:] + [cave]
        routes.extend(get_routes(cave, next_visited, visitable_twice))
    return routes


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def visitable(cave, visited, visitable_twice):
    if cave.is_large:
        return True
    elif cave == visitable_twice and visited.count(cave) < 2:
        return True
    else:
        return cave not in visited


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
