from functools import reduce


def main(raw_input):
    busses = parse_input(raw_input)

    # constraint stored in the form bus: t offset
    constraints = {}
    for i in range(len(busses)):
        if busses[i] != 'x':
            constraints[busses[i]] = i

    return chinese_remainder(constraints.keys(), [-i for i in constraints.values()])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    busses = raw_input.splitlines()[1].split(',')
    for i in range(len(busses)):
        if busses[i].isnumeric():
            busses[i] = int(busses[i])
    return busses


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
