import math


def main(raw_input):
    # Get the adaptors and add the "virtual adaptors" of the socket at the start and the phone at the end.
    adaptors = parse_input(raw_input)
    adaptors.insert(0, 0)
    adaptors.append(max(adaptors) + 3)

    # Get a list of increments from one adapter to the next
    differences = [adaptors[i + 1] - adaptors[i] for i in range(len(adaptors) - 1)]

    # Adapters with a jump of three jolts between them are fixed points in the chain. Everywhere between these can vary.
    # Get list of sub-chains which are variable sections of the chain (first and last elements are the fixed points).
    variable_chains = get_variable_chains(adaptors, differences)

    # Calculate the number of possible variations in each variable sub-chain. The product of all of these is the total
    # number of possible variations in the chain.
    variations = math.prod([count_valid_variations(chain[1:], [chain[0]], max(chain)) for chain in variable_chains])

    print(variations)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return sorted([int(i) for i in raw_input.splitlines()])


def get_variable_chains(adaptors, differences):
    variable_chains = []
    last_fixed = 0
    for i in range(len(differences)):
        if differences[i] == 3:
            variable_chains.append(adaptors[last_fixed:i + 1])
            last_fixed = i + 1

    return [chain for chain in variable_chains if len(chain) >= 3]


def count_valid_variations(adaptors, current_chain, target_jolts):
    valid_count = 0
    while True:
        next_adaptor = adaptors.pop(0)
        if next_adaptor > current_chain[-1] + 3:
            return valid_count
        elif next_adaptor == target_jolts:
            return valid_count + 1
        else:
            valid_count += count_valid_variations(adaptors[:], current_chain[:] + [next_adaptor], target_jolts)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
