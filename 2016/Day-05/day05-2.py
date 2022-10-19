from hashlib import md5
from tqdm import tqdm


def main(raw_input):
    door_id = raw_input.strip('\n')

    password = ["_", "_", "_", "_", "_", "_", "_", "_"]
    i = 0
    solved = 0
    while solved < 8:
        if md5((door_id + str(i)).encode()).hexdigest().startswith('00000'):
            md5hash = md5((door_id + str(i)).encode()).hexdigest()
            pos = md5hash[5]
            val = md5hash[6]
            if pos.isnumeric() and int(pos) < 8:
                if password[int(pos)] == "_":
                    solved += 1
                    password[int(pos)] = val
                    print("".join(password))
        i += 1

    print()
    return "".join(password)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
