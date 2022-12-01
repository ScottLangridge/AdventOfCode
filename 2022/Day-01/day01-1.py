def main(raw_input):
    elves = raw_input.split('\n\n')
    calories = [map(int, i.splitlines()) for i in elves]
    sum_calories = [sum(i) for i in calories]
    return max(sum_calories)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
