def main(raw_input):
    data = [int(x) for x in parse_input(raw_input)]

    for noun in range(100):
        for verb in range(100):
            if run_machine(data[:], noun, verb) == 19690720:
                return (100 * noun) + verb


def run_machine(data, noun, verb):
    data[1] = noun
    data[2] = verb

    pos = 0
    while data[pos] != 99:

        if data[pos] == 1:
            data[data[pos + 3]] = data[data[pos + 1]] + data[data[pos + 2]]
        elif data[pos] == 2:
            data[data[pos + 3]] = data[data[pos + 1]] * data[data[pos + 2]]

        pos += 4

    return data[0]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('../input.txt')
    print(main(puzzle_input))
