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
    calculation_area = []
    area_count = [0] * len(puzzle_input)

    # For each cell
    y = calculation_extremes[2]
    while y <= calculation_extremes[3]:
        calculation_area.append([])
        x = calculation_extremes[0]
        while x <= calculation_extremes[1]:
            # Get closest, write it in and add one to that numbers count
            closest = get_closest(x, y, puzzle_input)
            calculation_area[-1].append(closest)
            x += 1
        y += 1

    # Find values which are infinite
    infinites = []
    for i in calculation_area[0]:
        if i not in infinites:
            infinites.append(i)
    for i in calculation_area[-1]:
        if i not in infinites:
            infinites.append(i)
    for row in calculation_area:
        if row[0] not in infinites:
            infinites.append(row[0])
        if row[-1] not in infinites:
            infinites.append(row[-1])
    if -1 in infinites:
        infinites.remove(-1)

    max_count = 0
    for i in range(len(puzzle_input)):
        if i not in infinites:
            count = 0
            for row in calculation_area:
                for val in row:
                    if val == i:
                        count += 1
            if count > max_count:
                max_count = count
    return max_count


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
