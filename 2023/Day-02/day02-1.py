def main(raw_input):

    return sum([id_if_possible({'red': 12, 'green': 13, 'blue': 14}, i) for i in raw_input.splitlines()])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def id_if_possible(total_cubes, str_game):
    game_split = str_game.split(': ')
    game_id = int(game_split[0].strip('Game '))
    reveals = game_split[1].split('; ')
    for reveal in reveals:
        for colour_count in reveal.split(', '):
            colour_split = colour_count.split(' ')
            count = int(colour_split[0])
            colour = colour_split[1]
            if count > total_cubes[colour]:
                return 0
    return game_id



if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
