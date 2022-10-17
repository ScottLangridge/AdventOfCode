class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.cycle_length = fly_time + rest_time
        self.cycle_dist = speed * fly_time
        self.points = 0

    def distance_covered(self, time):
        full_cycles = int(time // self.cycle_length)
        remainder = time % self.cycle_length
        if remainder >= self.fly_time:
            return self.cycle_dist * full_cycles + self.speed * self.fly_time
        else:
            return self.cycle_dist * full_cycles + self.speed * remainder


def main(raw_input):
    reindeers = [get_reindeer(x) for x in raw_input.splitlines()]

    for i in range(1, 2503):
        winning = max(map(lambda x: x.distance_covered(i), reindeers))
        for reindeer in reindeers:
            if reindeer.distance_covered(i) == winning:
                reindeer.points += 1

    return max(map(lambda x: x.points, reindeers))


def get_reindeer(string):
    tokens = string.split()
    return Reindeer(tokens[0], int(tokens[3]), int(tokens[6]), int(tokens[13]))


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
