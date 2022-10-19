from collections import Counter


def main(raw_input):
    valid_room_strings = list(filter(lambda i: is_valid(i), raw_input.strip('\n').split('\n')))

    decrypted_room_strings = {}
    for string in valid_room_strings:
        decrypted_room_strings[decrypt(string)] = sector_id(string)

    return decrypted_room_strings["northpole-object-storage"]


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


def decrypt(string):
    shift_by = sector_id(string) % 26
    split_string = string.split('-')
    room_name = "-".join(split_string[:-1])

    decrypted_name = ""
    for c in room_name:
        if c == "-":
            decrypted_name += "-"
        else:
            decrypted_name += chr(ord("a") + (((ord(c) - ord("a")) + shift_by) % 26))

    return decrypted_name


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
