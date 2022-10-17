def main(raw_input):
    fish = [int(x) for x in raw_input.split(',')]

    for _ in range(80):
        fish = increment_fish(fish)

    return len(fish)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def increment_fish(fish):
    fish_out = []
    for i in fish:
        if i > 0:
            fish_out.append(i - 1)
        else:
            fish_out.append(6)
            fish_out.append(8)
    return fish_out


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
