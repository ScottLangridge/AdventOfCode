from itertools import permutations


def main(raw_input):
    numbers = [list(map(int, i.split())) for i in raw_input.strip('\n').split('\n')]
    numbers_transpose = list(zip(*numbers))
    joined_numbers_transpose = [num for sublist in numbers_transpose for num in sublist]

    valid_count = 0
    for i in range(0, len(joined_numbers_transpose), 3):
        t = joined_numbers_transpose[i:i + 3]
        if t[0] + t[1] > t[2] and t[1] + t[2] > t[0] and t[2] + t[0] > t[1]:
            valid_count += 1

    return valid_count


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
