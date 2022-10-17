def main(raw_input):
    current_pwd = raw_input

    for i in range(2):
        current_pwd = increment_pwd(current_pwd)
        while not valid(current_pwd):
            current_pwd = increment_pwd(current_pwd)

    return current_pwd


def increment_pwd(pwd):
    pwd = list(pwd)
    i = -1

    # Handle z
    while pwd[i] == 'z':
        pwd[i] = 'a'
        i -= 1

    # Skip "ambiguous" letters
    pwd[i] = increment_char(pwd[i])
    while pwd[i] in 'iol':
        pwd[i] = increment_char(pwd[i])

    return ''.join(pwd)


def increment_char(char):
    return chr(97 + (((ord(char) - 97) + 1) % 26))


def valid(pwd):
    if 'i' in pwd or 'o' in pwd or 'l' in pwd:
        raise RuntimeError('Should never generate a password with an "ambiguous" letter')

    i = 1
    double_count = 0
    while i < len(pwd):
        if pwd[i] == pwd[i - 1]:
            double_count += 1
            i += 1
        i += 1
    if double_count < 2:
        return False

    for i in range(len(pwd) - 2):
        if pwd[i] > 'x':
            continue
        if ord(pwd[i]) == ord(pwd[i + 1]) - 1 == ord(pwd[i + 2]) - 2:
            return True

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
