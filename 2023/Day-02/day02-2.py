def main(raw_input):

    return sum([min_set_power(i) for i in raw_input.splitlines()])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def min_set_power(str_game):
    min_set = {'red': 0, 'green': 0, 'blue': 0}

    game_split = str_game.split(': ')
    game_id = int(game_split[0].strip('Game '))
    reveals = game_split[1].split('; ')
    for reveal in reveals:
        for colour_count in reveal.split(', '):
            colour_split = colour_count.split(' ')
            count = int(colour_split[0])
            colour = colour_split[1]
            if min_set[colour] < count:
                min_set[colour] = count

    return min_set['red'] * min_set['green'] * min_set['blue']


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
