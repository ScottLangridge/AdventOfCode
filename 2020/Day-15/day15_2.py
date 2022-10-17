from collections import defaultdict


def main(raw_input):
    start_nums = parse_input(raw_input)

    t = 1
    memory = defaultdict(list)
    spoken_number = start_nums[-1]
    while start_nums:
        memory[start_nums.pop(0)].append(t)
        t += 1

    while t <= 30000000:
        if len(memory[spoken_number]) >= 2:
            spoken_number = memory[spoken_number][-1] - memory[spoken_number][-2]
            memory[spoken_number].append(t)
        else:
            memory[0].append(t)
            spoken_number = 0
        t += 1

    return spoken_number


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [int(num) for num in raw_input.split(',')]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
