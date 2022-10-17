import json
import re


def main(raw_input):
    tree = json.loads(raw_input)
    tree = del_reds(tree)
    return sum([int(x) for x in re.findall(r'-?\d+', json.dumps(tree))])


def del_reds(node):
    if type(node) == int or type(node) == str:
        return node
    if type(node) == dict:
        if 'red' in node.values():
            return 'deleted_node'
        else:
            return [del_reds(x) for x in node.values()]
    return [del_reds(x) for x in node]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
