# Would have taken four days

from datetime import datetime


def main(raw_input):
    busses = parse_input(raw_input)

    # constraint stored in the form bus: t offset
    constraints = {}
    for i in range(len(busses)):
        if busses[i] != 'x':
            constraints[busses[i]] = i

    slowest_bus = max(constraints.keys())
    slow_offset = constraints[slowest_bus]
    earliest_leave = 100000000000000

    i = earliest_leave
    while i % slowest_bus != 0:
        i += 1
    earliest_t = i - slow_offset

    t = earliest_t
    iterations = 0
    while not time_matches_constraints(constraints, t):
        t += slowest_bus
        iterations += 1

    return t


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    busses = raw_input.splitlines()[1].split(',')
    for i in range(len(busses)):
        if busses[i].isnumeric():
            busses[i] = int(busses[i])
    return busses


def time_matches_constraints(constraints, t):
    for i in constraints.keys():
        if (t + constraints[i]) % i != 0:
            return False
    return True


if __name__ == '__main__':
    time = datetime.now()
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
