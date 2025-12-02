def main(raw_input):
    invalid_sum = 0

    for r in raw_input.split(","):
        start, end = r.split("-")

        for id in range(int(start), int(end) + 1):
            str_id = str(id)
            longest_substring = len(str_id) // 2

            for l in range(1, longest_substring + 1):
                repeating_unit = str_id[:l]
                rebuilt_str = repeating_unit + repeating_unit
                while len(rebuilt_str) < len(str_id):
                    rebuilt_str += repeating_unit

                if rebuilt_str == str_id:
                    print("invalid: " + str_id)
                    invalid_sum += id
                    break

    return invalid_sum


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
