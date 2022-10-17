def main(raw_input):
    group_responses = parse_input(raw_input)
    group_yes_counts = [len(i) for i in group_responses]
    total_yes_count = sum(group_yes_counts)

    return total_yes_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    groups = [i.replace('\n', '') for i in raw_input.split('\n\n')]
    return ["".join(set(i)) for i in groups]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
