import itertools
from collections import defaultdict


def main(raw_input):
    rules, my_ticket, nearby_tickets = parse_input(raw_input)
    rules = combine_rules(rules)

    error_rate = 0
    for rule in rules:
        for ticket in nearby_tickets:
            for val in ticket:
                if not rule[0] <= val <= rule[1]:
                    error_rate += val

    return error_rate


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    rules, my_ticket, nearby_tickets = raw_input.split('\n\n')

    # Convert rules to a list of tuples containing (lower bound, upper bound).
    rules = rules.splitlines()
    rules = list(itertools.chain.from_iterable([rule.split(': ')[1].split(' or ') for rule in rules]))
    rules = [tuple(map(int, rule.split('-'))) for rule in rules]

    # Convert my ticket to a list of ints.
    my_ticket = [int(i) for i in my_ticket.splitlines()[1].split(',')]

    # Convert nearby_tickets to a list of lists of ints.
    nearby_tickets = nearby_tickets.splitlines()[1:]
    nearby_tickets = [[int(i) for i in ticket.split(',')] for ticket in nearby_tickets]

    return rules, my_ticket, nearby_tickets


def combine_rules(rules):
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


def ticket_is_valid(rules, ticket):
    for rule in rules:
        for val in ticket:
            if not (rule[0] <= val <= rule[1]):
                return False
    return True


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
