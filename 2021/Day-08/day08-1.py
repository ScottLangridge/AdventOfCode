def main(raw_input):
    split_input = [x.split(' | ') for x in raw_input.splitlines()]
    output_vals = []
    for x in split_input:
        output_vals.extend(x[1].split())

    easy_output_vals = list(filter(lambda x: len(x) in [2, 3, 4, 7], output_vals))

    return len(easy_output_vals)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
