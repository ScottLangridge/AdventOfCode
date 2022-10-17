def main(raw_input):
    seats = parse_input(raw_input)
    new_seats = update_seats(seats)

    while seats != new_seats:
        seats = new_seats
        new_seats = update_seats(seats)

    occupied_count = 0
    for row in new_seats:
        for seat in row:
            if seat == '#':
                occupied_count += 1

    return occupied_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return [list(line) for line in raw_input.splitlines()]


def update_seats(seats):
    rows_count = len(seats)
    row_width = len(seats[0])

    new_seats = []
    for y in range(rows_count):
        new_row = []
        for x in range(row_width):
            new_row.append(update_seat(seats, y, x))
        new_seats.append(new_row)
    return new_seats


def update_seat(seats, seat_y, seat_x):
    rows_count = len(seats)
    row_width = len(seats[0])

    seat_state = seats[seat_y][seat_x]
    if seat_state == '#':
        occupied = -1
    elif seat_state == 'L':
        occupied = 0
    else:
        return '.'

    for y in range(-1, 2):
        for x in range(-1, 2):
            if not (0 <= seat_x + x < row_width and 0 <= seat_y + y < rows_count):
                continue

            if seats[seat_y + y][seat_x + x] == '#':
                occupied += 1
            elif seats[seat_y + y][seat_x + x] == '.':
                occupied += seat_in_sight_occupied(seats, seat_y, seat_x, y, x)

    if seat_state == '#' and occupied >= 5:
        return 'L'
    elif seat_state == 'L' and occupied == 0:
        return '#'
    else:
        return seat_state


def seat_in_sight_occupied(seats, seat_y, seat_x, y_direction, x_direction):
    row_count = len(seats)
    row_width = len(seats[0])

    x = seat_x + x_direction
    y = seat_y + y_direction

    while True:
        if not (0 <= y < row_count and 0 <= x < row_width):
            return 0
        elif seats[y][x] == 'L':
            return 0
        elif seats[y][x] == '#':
            return 1

        x += x_direction
        y += y_direction


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
