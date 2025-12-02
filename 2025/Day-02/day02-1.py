def main(raw_input):
    invalid_sum = 0

    for r in raw_input.split(","):
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            str_i = str(i)

            if len(str_i) % 2 == 1:
                continue
            if str_i[:len(str_i)//2] == str_i[len(str_i)//2:]:
                print("invalid: " + str_i)
                invalid_sum += i

    return invalid_sum


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
