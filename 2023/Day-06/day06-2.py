from tqdm import tqdm


def main(raw_input):
    times, dists = raw_input.splitlines()
    t = int(times.strip('Time: ').replace(' ', ''))
    d = int(dists.strip('Distance: ').replace(' ', ''))

    winning_options = 0
    for btn_time in tqdm(range(t + 1)):
        if get_dist(t, btn_time) > d:
            winning_options += 1

    return winning_options


def get_dist(race_time, btn_time):
    return btn_time * (race_time - btn_time)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
