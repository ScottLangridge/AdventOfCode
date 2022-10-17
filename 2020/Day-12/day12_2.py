def main(raw_input):
    compass_headings = {'N': 0, 'E': 90, 'S': 180, 'W': 270}

    route = parse_input(raw_input)
    pos_x, pos_y = 0, 0
    way_dx, way_dy = 10, -1

    for i in route:
        if i[0] == 'L' or i[0] == 'R':
            way_dx, way_dy = rotate_waypoint(i, way_dx, way_dy)
        elif i[0] == 'F':
            pos_x, pos_y = move_ship(pos_x, pos_y, way_dx, way_dy, i[1])
        else:
            way_dx, way_dy = move_waypoint(way_dx, way_dy, compass_headings[i[0]], i[1])

    return abs(pos_x) + abs(pos_y)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [[i[0], int(i[1:])] for i in raw_input.splitlines()]


def move_ship(pos_x, pos_y, way_dx, way_dy, iterations):
    pos_x += way_dx * iterations
    pos_y += way_dy * iterations
    return pos_x, pos_y


def move_waypoint(way_dx, way_dy, heading, distance):
    if heading == 0:
        return way_dx, way_dy - distance
    elif heading == 90:
        return way_dx + distance, way_dy
    elif heading == 180:
        return way_dx, way_dy + distance
    elif heading == 270:
        return way_dx - distance, way_dy


def rotate_waypoint(instruction, way_dx, way_dy):
    iterations = instruction[1] // 90

    # True = +ve, False = -ve
    signs_transformations_left = {
        (False, False): (False, True),
        (False, True): (True, True),
        (True, True): (True, False),
        (True, False): (False, False)
    }

    signs_transformations_right = {
        (False, True): (False, False),
        (True, True): (False, True),
        (True, False): (True, True),
        (False, False): (True, False)
    }

    for i in range(iterations):
        signs = coords_to_signs(way_dx, way_dy)
        if instruction[0] == 'L':
            new_signs = signs_transformations_left[signs]
        else:
            new_signs = signs_transformations_right[signs]

        temp = way_dx
        way_dx = way_dy
        way_dy = temp
        way_dx, way_dy = apply_signs((way_dx, way_dy), new_signs)

    return way_dx, way_dy


def coords_to_signs(x, y):
    return x >= 0, y >= 0


def apply_signs(coords, signs):
    out = []
    for i in range(2):
        if signs[i]:
            out.append(abs(coords[i]))
        else:
            out.append(-abs(coords[i]))
    return out


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
