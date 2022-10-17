from collections import defaultdict


def main(raw_input):
    can_contain_colour = parse_rules(raw_input)
    possible_parents = get_possible_parents(can_contain_colour, 'shiny gold')

    return len(possible_parents)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_rules(raw_input):
    # Rules are in the form {bag colour: [bag colours which can contain it, ...]}

    minimised_input = raw_input.replace(' bags', '').replace(' bag', '').replace('.', '')

    rules_dict = defaultdict(list)
    for i in minimised_input.splitlines():
        bag_colour, contains_string = i.split(' contain ')

        if contains_string == 'no other':
            contained_colours = []
        else:
            contains_lst = contains_string.split(', ')
            contained_colours = [i[2:] for i in contains_lst]

        for contained_colour in contained_colours:
            rules_dict[contained_colour].extend([bag_colour])

    return rules_dict


def get_possible_parents(can_contain_colour, colour):
    direct_parents = can_contain_colour[colour]

    indirect_parents = []
    for parent_colour in direct_parents:
        indirect_parents.extend(get_possible_parents(can_contain_colour, parent_colour))

    return set(direct_parents + indirect_parents)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
