def main(raw_input):
    times, dists = raw_input.splitlines()
    times = [int(i) for i in times.strip('Time: ').split()]
    dists = [int(i) for i in dists.strip('Distance: ').split()]
    races = zip(times, dists)

    prod_winning_options = 1
    for t, d in races:
        winning_options = 0
        for btn_time in range(t + 1):
            if get_dist(t, btn_time) > d:
                winning_options += 1
        prod_winning_options *= winning_options

    return prod_winning_options


def get_dist(race_time, btn_time):
    return btn_time * (race_time - btn_time)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
