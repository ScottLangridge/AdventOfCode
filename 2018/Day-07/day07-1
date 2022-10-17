import time
from collections import defaultdict


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        line = line.strip('\n').split(' ')
        out.append([line[1], line[7]])
    return out


def solve(puzzle_input):
    final_order = ''
    dependants = {}
    for i in range(65, 91):
        dependants[chr(i)] = []
    for pair in puzzle_input:
        dependants[pair[1]].append(pair[0])

    while len(dependants) > 0:
        ready = []
        for step in dependants.keys():
            if len(dependants[step]) == 0:
                ready.append(step)
        ready.sort()

        dependants.pop(ready[0])
        final_order = final_order + ready[0]

        for step in dependants.keys():
            if ready[0] in dependants[step]:
                lst = dependants[step]
                lst.remove(ready[0])
                dependants[step] = lst
                if dependants[step] is None:
                    dependants[step] = []

    return final_order




start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
