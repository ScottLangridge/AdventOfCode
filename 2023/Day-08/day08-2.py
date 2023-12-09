# I know this solution is very slow, but it's the one I came up with using no hints from the
# subreddit. I missed the fact that first_finish always = period, so LCM does work.
#
# As slower implementations that don't require first_finish == period go, I think this is pretty
# well optimised.


class NodeMap:
    def __init__(self, str_raw_map):
        self.mappings = {}
        for i in str_raw_map.splitlines():
            start, left, right = i.replace(' = (', ',').replace(' ', '').replace(')', '').split(',')
            self.mappings[start] = (left, right)

    def next_node(self, current_node, instruction):
        return self.mappings[current_node][instruction]


class Instructions:
    def __init__(self, str_raw_instructions):
        self.sequence = [int(i) for i in str_raw_instructions.replace('L', '0').replace('R', '1')]
        self.length = len(self.sequence)

    def at(self, index):
        return self.sequence[index % self.length]


class NodePath:
    def __init__(self, node_map, instructions, start_node):
        self.node_map = node_map
        self.instructions = instructions
        self.start_node = start_node
        self.end_node = None
        self.first_finish = None
        self.period = None

        self.find_first_finish()
        self.find_second_finish()
        self.find_third_finish()

        self.i = self.first_finish

    def loop(self):
        self.i += self.period

    def find_first_finish(self):
        i = 0
        current_node = self.start_node
        while not is_finish_node(current_node):
            current_node = self.node_map.next_node(current_node, self.instructions.at(i))
            i += 1

        self.end_node = current_node
        self.first_finish = i

    def find_second_finish(self):
        i = self.first_finish + 1
        current_node = self.node_map.next_node(self.end_node, self.instructions.at(i))
        while not is_finish_node(current_node):
            current_node = self.node_map.next_node(current_node, self.instructions.at(i))
            i += 1

        assert current_node == self.end_node
        assert self.instructions.at(i) == self.instructions.at(self.first_finish)
        self.period = i - self.first_finish

    def find_third_finish(self):
        i = self.first_finish + self.period + 1
        current_node = self.node_map.next_node(self.end_node, self.instructions.at(i))
        while not is_finish_node(current_node):
            current_node = self.node_map.next_node(current_node, self.instructions.at(i))
            i += 1

        assert current_node == self.end_node
        assert self.instructions.at(i) == self.instructions.at(self.first_finish)
        assert i == self.first_finish + self.period + self.period


def is_finish_node(node):
    return node[-1] == 'Z'


def finished(current_nodes):
    for node in current_nodes:
        if node[-1] != 'Z':
            return False
    return True


def main(raw_input):
    # Parse Input
    raw_instructions, raw_map = raw_input.split('\n\n')

    instructions = Instructions(raw_instructions)
    node_map = NodeMap(raw_map)

    # path = NodePath(node_map, instructions, 'AAA')
    # return path.first_finish

    start_nodes = list(filter(lambda node: node[-1] == 'A', node_map.mappings.keys()))
    paths = [NodePath(node_map, instructions, node) for node in start_nodes]

    steps = 0
    while not all_paths_match(paths):
        min(paths, key=lambda path: path.i).loop()

        if steps % 1000000 == 0:
            print([path.i for path in paths])
        steps += 1

    return paths[0].i


def all_paths_match(paths):
    i_0 = paths[0].i
    for path in paths[1:]:
        if path.i != i_0:
            return False
    return True


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
