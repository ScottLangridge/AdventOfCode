from collections import defaultdict


def main(raw_input):
    can_be_contained_by_colour = parse_rules(raw_input)
    return count_children(can_be_contained_by_colour, 'shiny gold')


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_rules(raw_input):
    # Rules are in the form {bag colour: [(colour it must contain, quantity), ...]}

    minimised_input = raw_input.replace(' bags', '').replace(' bag', '').replace('.', '')

    rules_dict = defaultdict(list)
    for i in minimised_input.splitlines():
        bag_colour, contains_string = i.split(' contain ')

        contained_colours = []
        if contains_string != 'no other':
            contents = contains_string.split(', ')
            for item in contents:
                item_count = int(item.split(' ')[0])
                item_colour = ' '.join(item.split(' ')[1:])
                contained_colours.append((item_colour, item_count))

        rules_dict[bag_colour].extend(contained_colours)

    return rules_dict


def count_children(can_be_contained_by_colour, colour):
    total_children = 0
    for child in can_be_contained_by_colour[colour]:
        # Add the child bag
        total_children += child[1]
        # Add the children of the child bag
        total_children += child[1] * count_children(can_be_contained_by_colour, child[0])
    return total_children


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
