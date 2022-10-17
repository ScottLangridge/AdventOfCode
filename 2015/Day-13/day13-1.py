from itertools import permutations


def main(raw_input):
    modifiers = [parse_line(line) for line in raw_input.splitlines()]
    modifiers_dict = {}
    for mod in modifiers:
        modifiers_dict[(mod[0], mod[1])] = mod[2]
    people = set(map(lambda x: x[0], modifiers))

    best_happiness = 0
    for perm in permutations(people):
        perm_happiness = get_happiness(perm, modifiers_dict)
        if perm_happiness > best_happiness:
            best_happiness = perm_happiness

    # Return solution
    return best_happiness


def parse_line(string):
    tokens = string.split()
    if tokens[2] == 'gain':
        return [tokens[0], tokens[-1].strip('.'), int(tokens[3])]
    else:
        return [tokens[0], tokens[-1].strip('.'), int('-' + tokens[3])]


def get_happiness(permutation, modifiers_dict):
    happiness = 0
    for i in range(len(permutation)):
        happiness += modifiers_dict[(permutation[i], permutation[(i + 1) % len(permutation)])]
        happiness += modifiers_dict[(permutation[i], permutation[(i - 1) % len(permutation)])]
    return happiness


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
