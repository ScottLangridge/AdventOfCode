def main(raw_input):
    forest = [list(map(int, line)) for line in raw_input.splitlines()]
    max_y = len(forest)
    max_x = len(forest[0])

    visible_count = 0
    best_score = 0
    for y in range(max_y):
        for x in range(max_x):
            score = scenic_score(forest, x, y, max_x, max_y)
            if score > best_score:
                best_score = score

    return best_score


def scenic_score(forest, tree_x, tree_y, max_x, max_y):
    if tree_x == 0 or tree_x == max_x - 1 or tree_y == 0 or tree_y == max_y - 1:
        return 0

    height = forest[tree_y][tree_x]
    views = []

    view_score = 0
    x = tree_x + 1
    while x < max_x:
        view_score += 1
        if forest[tree_y][x] >= height:
            break
        x += 1
    views.append(view_score)

    view_score = 0
    x = tree_x - 1
    while x >= 0:
        view_score += 1
        if forest[tree_y][x] >= height:
            break
        x -= 1
    views.append(view_score)

    view_score = 0
    y = tree_y + 1
    while y < max_y:
        view_score += 1
        if forest[y][tree_x] >= height:
            break
        y += 1
    views.append(view_score)

    view_score = 0
    y = tree_y - 1
    while y >= 0:
        view_score += 1
        if forest[y][tree_x] >= height:
            break
        y -= 1
    views.append(view_score)

    return views[0] * views[1] * views[2] * views[3]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
