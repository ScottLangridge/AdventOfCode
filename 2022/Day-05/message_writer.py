from random import randint, choice


def write(message, min_column=10, max_column=50, steps=10000):
    final_stacks = []
    for i in range(len(message)):
        stack = []
        for _ in range(randint(min_column, max_column)):
            stack.append(choice('abcdefghijklmnopqrstuvwxyz_'))
        stack.append(message[i])
        final_stacks.append(stack)

    inital_stacks, instructions = scramble(final_stacks, steps)

    print_stacks(inital_stacks, instructions)


def scramble(stacks, steps):
    instructions = []

    stack_count = len(stacks)
    for i in range(steps):
        move_from = randint(1, stack_count)
        while len(stacks[move_from - 1]) == 0:
            move_from = randint(1, stack_count)
        move_to = randint(1, stack_count)
        move_num = randint(1, len(stacks[move_from - 1]))
        instructions.append(f'move {str(move_num)} from {int_to_chr(move_to)} to {int_to_chr(move_from)}')
        stacks[move_to - 1].extend(pop_n(stacks[move_from - 1], move_num))

    return stacks, reversed(instructions)


def pop_n(lst, n):
    out = reversed(lst[-n:])
    del lst[-n:]
    return out


def int_to_chr(i):
    return i
    # return chr(i + 96)


def print_stacks(stacks, instructions):
    stack_count = len(stacks)
    tallest_stack = max(map(len, stacks))
    for i in range(len(stacks)):
        while len(stacks[i]) < tallest_stack:
            stacks[i].append(' ')

    stacks = list(map(lambda i: list(reversed(i)), stacks))

    stacks = list(zip(*stacks))

    stacks = list(map(lambda i: '[' + '] ['.join(i) + ']', stacks))
    stacks = list(map(lambda i: i.replace('[ ]', '   '), stacks))

    stacks = '\n'.join(stacks)
    stacks += '\n'

    i = 1
    while i <= stack_count:
        stacks += f' {int_to_chr(i)}  '
        i += 1
    stacks = stacks[:-1]

    with open('super_input.txt', 'w+') as f:
        f.write(stacks)
        f.write('\n\n')
        f.write('\n'.join(instructions))


def parse_stacks(str_stacks):
    stacks = [i.strip('[]').split(',') for i in str_stacks.replace('    ', ' []').replace('] [', ',').splitlines()][:-1]
    return [list(filter(lambda i: i != '', reversed(stack))) for stack in zip(*stacks)]


write("nevergonnagiveyouup", 10, 10, 2)
