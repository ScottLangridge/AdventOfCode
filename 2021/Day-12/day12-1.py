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

    routes = get_routes(caves['start'], [caves['start']])
    non_deadend_routes = list(filter(lambda x: x[-1].id == 'end', routes))

    return len(non_deadend_routes)


def get_cave(caves, cave_id):
    if cave_id not in caves.keys():
        caves[cave_id] = Cave(cave_id)
    return caves[cave_id]


def get_routes(current, visited):
    reachable = [cave for cave in current.connections if cave not in visited or cave.is_large]

    if not reachable or current.id == 'end':
        return [visited]

    routes = []
    for cave in reachable:
        next_visited = visited[:] + [cave]
        routes.extend(get_routes(cave, next_visited))
    return routes


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
