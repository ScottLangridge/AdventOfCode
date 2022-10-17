def main(raw_input):

    compass_headings = {'N': 0, 'E': 90, 'S': 180, 'W': 270}

    route = parse_input(raw_input)
    pos_x, pos_y = 0, 0
    heading = 90

    for i in route:
        if i[0] == 'L':
            heading = (heading - i[1]) % 360
        elif i[0] == 'R':
            heading = (heading + i[1]) % 360
        elif i[0] == 'F':
            pos_x, pos_y = move(pos_x, pos_y, heading, i[1])
        else:
            pos_x, pos_y = move(pos_x, pos_y, compass_headings[i[0]], i[1])

    return abs(pos_x) + abs(pos_y)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [[i[0], int(i[1:])] for i in raw_input.splitlines()]


def move(pos_x, pos_y, heading, distance):
    if heading == 0:
        return pos_x, pos_y - distance
    elif heading == 90:
        return pos_x + distance, pos_y
    elif heading == 180:
        return pos_x, pos_y + distance
    elif heading == 270:
        return pos_x - distance, pos_y


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
