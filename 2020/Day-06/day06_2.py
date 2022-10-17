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
    groups = [i.split('\n') for i in raw_input.split('\n\n')]
    return [get_group_intersection(i) for i in groups]


def get_group_intersection(group):
    answers_in_common = group.pop()
    while len(group) > 0:
        answers_in_common = get_list_intersection(answers_in_common, group.pop())
    return answers_in_common


def get_list_intersection(lst1, lst2):
    return [i for i in lst1 if i in lst2]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
