import itertools
from collections import defaultdict


def main(raw_input):
    rules, combined_rules, my_ticket, nearby_tickets = parse_input(raw_input)
    nearby_tickets = list(filter(lambda t: ticket_is_valid(combined_rules, t), nearby_tickets))

    # Build a dict mapping ticket position indexes to the rules that match all valid tickets for that position
    position_count = len(my_ticket)
    valid_rules_by_pos = []
    for pos in range(position_count):
        pos_vals = []
        for ticket in nearby_tickets:
            pos_vals.append(ticket[pos])

        pos_rules = []
        for rule in rules.keys():
            if data_valid(rules[rule], pos_vals):
                pos_rules.append(rule)
        valid_rules_by_pos.append(pos_rules)

    # Where a rule is the only rule in the position, you can eliminate it from others. Do this until you have one rule
    # per position
    while len(list(itertools.chain.from_iterable(valid_rules_by_pos))) > position_count:
        for pos in valid_rules_by_pos:
            if len(pos) == 1:
                eliminate_duplicates_from_list(valid_rules_by_pos, pos[0])

    # Convert the list of positions and rules to a dict of rules to positions
    rule_positions = {}
    for pos in range(len(valid_rules_by_pos)):
        rule_positions[valid_rules_by_pos[pos][0]] = pos

    departure_rules = list(filter(lambda rule_name: rule_name.startswith('departure'), rules.keys()))
    departure_product = 1
    for rule in departure_rules:
        departure_product *= my_ticket[rule_positions[rule]]

    return departure_product


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    rules, my_ticket, nearby_tickets = raw_input.split('\n\n')

    # Convert rules to a list of tuples containing (lower bound, upper bound).
    rules = rules.splitlines()

    rule_dict = {}
    for rule in rules:
        rule = parse_rule(rule)
        rule_dict[rule[0]] = rule[1]

    combined_rules = combine_rules(rules)

    # Convert my ticket to a list of ints.
    my_ticket = [int(i) for i in my_ticket.splitlines()[1].split(',')]

    # Convert nearby_tickets to a list of lists of ints.
    nearby_tickets = nearby_tickets.splitlines()[1:]
    nearby_tickets = [[int(i) for i in ticket.split(',')] for ticket in nearby_tickets]

    return rule_dict, combined_rules, my_ticket, nearby_tickets


def parse_rule(rule):
    name, ranges = rule.split(': ')
    ranges = ranges.split(' or ')
    for i in (0, 1):
        ranges[i] = [int(val) for val in ranges[i].split('-')]
    return name, ranges


def combine_rules(rules):
    rules = list(itertools.chain.from_iterable([rule.split(': ')[1].split(' or ') for rule in rules]))
    rules = [tuple(map(int, rule.split('-'))) for rule in rules]

    combined_rules = defaultdict(list)
    for rule in rules:
        combined_rules[rule[0]].append('lb')
        combined_rules[rule[1]].append('ub')

    current_bound = 'lb'
    bound_stack = 0
    combined_bounds = []
    for boundary_val in sorted(combined_rules.keys()):
        for bound in sorted(combined_rules[boundary_val]):
            if bound == 'lb':
                if bound_stack == 0:
                    combined_bound_start = boundary_val
                bound_stack += 1
            else:
                bound_stack -= 1
                if bound_stack == 0:
                    combined_bounds.append((combined_bound_start, boundary_val))

    return combined_bounds


def ticket_is_valid(combined_rules, ticket):
    for rule in combined_rules:
        for val in ticket:
            if not (rule[0] <= val <= rule[1]):
                return False
    return True


def data_valid(rule, data):
    for val in data:
        if not ((rule[0][0] <= val <= rule[0][1]) or (rule[1][0] <= val <= rule[1][1])):
            return False
    return True


def eliminate_duplicates_from_list(lst, val):
    for i in range(len(lst)):
        if len(lst[i]) > 1:
            if val in lst[i]:
                lst[i].remove(val)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
