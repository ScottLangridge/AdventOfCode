import time


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        str_coord = line.strip('\n').split(',')
        out.append([int(str_coord[0]), int(str_coord[1])])
    return out


def solve(puzzle_input):
    calculation_extremes = find_extremes(puzzle_input)
    safe_points = 0

    # For each cell
    y = calculation_extremes[2]
    while y <= calculation_extremes[3]:
        x = calculation_extremes[0]
        while x <= calculation_extremes[1]:
            # Get closest, write it in and add one to that numbers count
            sum_dist = 0
            for point in puzzle_input:
                sum_dist += get_dist(x, y, point[0], point[1])
                if sum_dist > 10000:
                    break
            if sum_dist < 10000:
                safe_points += 1
            x += 1
        y += 1

    return safe_points


def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_closest(x, y, puzzle_input):
    least_dist = get_dist(x, y, puzzle_input[0][0], puzzle_input[0][1])
    closest_index = 0
    match = False
    for i, coord in enumerate(puzzle_input[1:]):
        dist = get_dist(x, y, coord[0], coord[1])
        if dist < least_dist:
            least_dist = dist
            closest_index = i + 1
            match = False
        elif dist == least_dist:
            match = True

    if match:
        return -1
    else:
        return closest_index


def find_extremes(puzzle_input):
    low_x = puzzle_input[0][0]
    high_x = puzzle_input[0][0]
    low_y = puzzle_input[0][1]
    high_y = puzzle_input[0][1]

    for coord in puzzle_input[1:]:
        x = coord[0]
        y = coord[1]

        if x < low_x: low_x = x - 1
        if y < low_y: low_y = y - 1
        if x > high_x: high_x = x + 1
        if x > high_y: high_y = y + 1

    return [low_x, high_x, low_y, high_y]


def get_margin_extremes(extremes):
    x_off = round((extremes[1] - extremes[0]) / 2) + 2
    y_off = round((extremes[3] - extremes[2]) / 2) + 2
    return extremes[0] - x_off, extremes[1] + x_off, extremes[2] - y_off, extremes[3] + y_off


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
