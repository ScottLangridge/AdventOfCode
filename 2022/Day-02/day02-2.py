1533


def main(raw_input):
    match = [i.split() for i in raw_input.strip().splitlines()]

    total_score = 0
    for game in match:
        total_score += score_game(*game)

    return total_score


def score_game(opponent_move, desired_outcome):
    beats = {'S': 'R', 'P': 'S', 'R': 'P'}
    beaten_by = {y: x for x, y in beats.items()}
    score = {'R': 1, 'P': 2, 'S': 3}

    opponent = {'A': 'R', 'B': 'P', 'C': 'S'}
    o = opponent[opponent_move]

    if desired_outcome == 'X':
        p = beaten_by[o]
    elif desired_outcome == 'Y':
        p = o
    else:
        p = beats[o]

    score = score[p]
    if beats[o] == p:
        score += 6
    elif p == o:
        score += 3

    return score


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
