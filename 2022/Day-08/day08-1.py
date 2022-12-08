def main(raw_input):
    forest = [list(map(int, line)) for line in raw_input.splitlines()]
    max_y = len(forest)
    max_x = len(forest[0])

    visible_count = 0
    for y in range(max_y):
        for x in range(max_x):
            if tree_visible(forest, x, y, max_x, max_y):
                visible_count += 1

    return visible_count


def tree_visible(forest, tree_x, tree_y, max_x, max_y):
    if tree_x == 0 or tree_x == max_x - 1 or tree_y == 0 or tree_y == max_y - 1:
        return True

    height = forest[tree_y][tree_x]

    obscuring_trees = []
    for x in range(tree_x):
        obscuring_trees.append(forest[tree_y][x])
    if max(obscuring_trees) < height:
        return True

    obscuring_trees = []
    for x in range(tree_x + 1, max_x):
        obscuring_trees.append(forest[tree_y][x])
    if max(obscuring_trees) < height:
        return True

    obscuring_trees = []
    for y in range(tree_y):
        obscuring_trees.append(forest[y][tree_x])
    if max(obscuring_trees) < height:
        return True

    obscuring_trees = []
    for y in range(tree_y + 1, max_y):
        obscuring_trees.append(forest[y][tree_x])
    if max(obscuring_trees) < height:
        return True

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
