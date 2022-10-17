import time


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    # print('Test:', solve(get_input('example2.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    with open(filepath, 'r') as f:
        raw = f.readline()
    out = raw.split(' ')
    out = list(map(int, out))
    return out


def get_node_tree(puzzle_input):
    node = ([], [])
    i = 0
    for branch in range(puzzle_input[0]):
        i += 2
        result = get_node_tree(puzzle_input[i:])
        node[0].append(result[0])
        i += result[1]
    for meta in range(puzzle_input[1]):
        node[1].append(puzzle_input[i + 2])
        i += 1
    return node, i


def get_node_val(node):
    if len(node[0]) == 0:
        return sum(node[1])
    else:
        total = 0
        for meta in node[1]:
            if 0 < meta <= len(node[0]):
                total += get_node_val(node[0][meta - 1])
        return total


def solve(puzzle_input):
    return get_node_val(get_node_tree(puzzle_input)[0])


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
