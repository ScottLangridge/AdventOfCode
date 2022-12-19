exec_out = None


def main(raw_input):
    pairs = [pair.split('\n') for pair in raw_input.strip().split('\n\n')]

    index = 0
    valid_pairs = 0
    for pair in pairs:
        index += 1
        if valid_pair(*pair):
            valid_pairs += index

    return valid_pairs


def valid_pair(l, r):
    global exec_out
    exec_out = []
    exec(f'global exec_out\nexec_out.append({l})')
    exec(f'global exec_out\nexec_out.append({r})')
    l, r = exec_out
    i = 0

    while True:
        if i == len(l) == len(r):
            return
        elif i == len(l):
            return True
        elif i == len(r):
            return False

        li = l[i]
        ri = r[i]

        if type(li) == list and type(ri) == int:
            r[i] = [ri]
            ri = r[i]
        elif type(li) == int and type(ri) == list:
            l[i] = [li]
            li = l[i]

        if type(li) == int:
            if li == ri:
                i += 1
            else:
                return li < ri
        else:
            result = valid_pair(li, ri)
            if result is not None:
                return result
            else:
                i += 1


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
