exec_out = None


def main(raw_input):
    packets = raw_input.strip().replace('\n\n', '\n').splitlines()
    packets.append([[2]])
    packets.append([[6]])

    print("Sorting... This will take some time.")
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(packets) - 1):
            if not in_order(packets[i], packets[i + 1]):
                ordered = False
                temp = packets[i]
                packets[i] = packets[i + 1]
                packets[i + 1] = temp

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def in_order(l, r):
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
            result = in_order(li, ri)
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
