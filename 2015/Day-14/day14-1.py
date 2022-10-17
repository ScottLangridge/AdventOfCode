class Reindeer:
    def __init__(self, name, speed, fly_time, rest_time):
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.cycle_length = fly_time + rest_time
        self.cycle_dist = speed * fly_time

    def distance_covered(self, time):
        full_cycles = int(time // self.cycle_length)
        remainder = time % full_cycles
        if remainder >= self.fly_time:
            return self.cycle_dist * full_cycles + self.speed * self.fly_time
        else:
            return self.cycle_dist * full_cycles + self.speed * remainder


def main(raw_input):
    reindeers = [get_reindeer(x) for x in raw_input.splitlines()]
    return max(map(lambda x: x.distance_covered(2503), reindeers))


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
