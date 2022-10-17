def main(raw_input):
    seat_coords = parse_boarding_passes(raw_input)
    seat_ids = [get_seat_id(i) for i in seat_coords]

    return max(seat_ids)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_boarding_passes(raw_input):
    seat_strings = raw_input.splitlines()

    seat_coords = []
    for i in seat_strings:
        row_bin = i[:7].replace('F', '0').replace('B', '1')
        col_bin = i[-3:].replace('L', '0').replace('R', '1')
        row_int = int(row_bin, 2)
        col_int = int(col_bin, 2)
        seat_coords.append((row_int, col_int))
    return seat_coords


def get_seat_id(seat_coordinate):
    return seat_coordinate[0] * 8 + seat_coordinate[1]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
