from itertools import permutations


def main(raw_input):
    dists = {}
    for line in raw_input.splitlines():
        location_1, location_2, dist = parse_line(line)
        dists[(location_1, location_2)] = dist
        dists[(location_2, location_1)] = dist
    locations = list(set(map(lambda x: x[0], dists.keys())))

    shortest_route_length = get_route_length(locations, dists)
    for i in permutations(locations):
        route_length = get_route_length(i, dists)
        if route_length < shortest_route_length:
            shortest_route_length = route_length

    return shortest_route_length


def get_route_length(route, dists):
    length = 0
    for i in range(len(route) - 1):
        length += dists[(route[i], route[i + 1])]
    return length


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_line(string):
    tokens = string.split()
    return tokens[0], tokens[2], int(tokens[4])


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
