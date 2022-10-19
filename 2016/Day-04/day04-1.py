from collections import Counter


def main(raw_input):
    room_strings = raw_input.strip('\n').split('\n')

    sector_id_sum = 0
    for string in room_strings:
        if is_valid(string):
            sector_id_sum += sector_id(string)

    return sector_id_sum


def is_valid(room_string):
    split_string = room_string.split('-')
    room_name = "".join(split_string[:-1])
    checksum = split_string[-1].split('[')[1][:-1]

    return checksum == get_checksum(room_name)


def get_checksum(string):
    counts = Counter(string)
    uniq_string = "".join(set(string))
    sorted_str = "".join(sorted(uniq_string, key=lambda i: (counts[i] * 1000) + (1000 - ord(i)), reverse=True))
    return sorted_str[:5]


def sector_id(string):
    return int(string.split("-")[-1].split("[")[0])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
