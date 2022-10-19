from hashlib import md5
from tqdm import tqdm


def main(raw_input):
    door_id = raw_input.strip('\n')

    progress = tqdm(total=8)
    password = ""
    i = 0
    while len(password) < 8:
        if md5((door_id + str(i)).encode()).hexdigest().startswith('00000'):
            password += md5((door_id + str(i)).encode()).hexdigest()[5]
            progress.update(len(password))
        i += 1
    progress.close()

    return password


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
