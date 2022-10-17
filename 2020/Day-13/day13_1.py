def main(raw_input):
    earliest_depart, busses = parse_input(raw_input)

    wait_time = {}
    for bus in busses:
        wait_time[bus - (earliest_depart % bus)] = bus

    least_wait = min(wait_time.keys())

    return least_wait * wait_time[least_wait]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    earliest_depart, busses = raw_input.splitlines()
    busses = busses.split(',')
    busses = list(filter(lambda a: a != 'x', busses))
    return int(earliest_depart), [int(bus) for bus in busses]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
