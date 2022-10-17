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
    row_count = len(seats)
    row_width = len(seats[0])

    new_seats = []
    for y in range(row_count):
        new_row = []
        for x in range(row_width):
            new_row.append(update_seat(seats, y, x))
        new_seats.append(new_row)
    return new_seats


def update_seat(seats, seat_y, seat_x):
    row_count = len(seats)
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
            if not (0 <= seat_x + x < row_width and 0 <= seat_y + y < row_count):
                continue

            if seats[seat_y + y][seat_x + x] == '#':
                occupied += 1

    if seat_state == '#' and occupied >= 4:
        return 'L'
    elif seat_state == 'L' and occupied == 0:
        return '#'
    else:
        return seat_state


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
