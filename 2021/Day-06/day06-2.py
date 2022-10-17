from collections import defaultdict


def main(raw_input):
    fish = [int(x) for x in raw_input.split(',')]

    fish_dict = defaultdict(int)
    for i in set(fish):
        fish_dict[i] = fish.count(i)

    for i in range(256):
        fish_dict = increment_fish(fish_dict)

    return sum(fish_dict.values())


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def increment_fish(fish_dict):
    # Decrement spawn timer
    for i in range(8 + 1):
        fish_dict[i - 1] = fish_dict[i]

    # Spawn new fish
    fish_dict[8] = fish_dict[-1]

    # Reset timers on parent fish
    fish_dict[6] += fish_dict[-1]
    del fish_dict[-1]

    return fish_dict



if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
