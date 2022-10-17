operators = {
    'AND': lambda x, y: x & y,
    'OR': lambda x, y: x | y,
    'LSHIFT': lambda x, n: x << n,
    'RSHIFT': lambda x, n: x >> n,
    'NOT': lambda x, _: int('0b' + bin(x)[2:].zfill(16).replace('0', '_').replace('1', '0').replace('_', '1'), 2),
    'SET': lambda x, _: x
}


def main(raw_input):
    instructions = [parse_instruction(i) for i in raw_input.splitlines()]

    i = 0
    wire_vals = {}

    while instructions:
        i %= len(instructions)
        if not ready_to_evaluate(instructions[i], wire_vals):
            i += 1
            continue

        evaluate(instructions.pop(i), wire_vals)

    override_with = wire_vals['a']

    instructions = [parse_instruction(i) for i in raw_input.splitlines()]
    instructions = list(filter(lambda x: x[-1] != 'b', instructions))
    instructions.append(['SET', override_with, None, 'b'])

    i = 0
    wire_vals = {}

    while instructions:
        i %= len(instructions)
        if not ready_to_evaluate(instructions[i], wire_vals):
            i += 1
            continue

        evaluate(instructions.pop(i), wire_vals)

    return wire_vals['a']


def parse_instruction(instruction):
    tokens = instruction.split()
    for i in range(len(tokens)):
        if tokens[i].isnumeric():
            tokens[i] = int(tokens[i])

    if tokens[1] in ['AND', 'OR']:
        return [tokens[1], tokens[0], tokens[2], tokens[4]]
    if tokens[1] in ['LSHIFT', 'RSHIFT']:
        return [tokens[1], tokens[0], int(tokens[2]), tokens[4]]
    elif tokens[0] == 'NOT':
        return ['NOT', tokens[1], None, tokens[3]]
    else:
        return ['SET', tokens[0], None, tokens[2]]


def ready_to_evaluate(instruction, wire_vals):
    for op in instruction[1:3]:
        if not (op is None or type(op) == int or op in wire_vals.keys()):
            return False
    return True


def evaluate(i, wire_vals):
    operator = i[0]
    operand1 = get_operand_val(i[1], wire_vals)
    operand2 = get_operand_val(i[2], wire_vals)
    wire_out = i[3]
    wire_vals[wire_out] = operators[operator](operand1, operand2)


def get_operand_val(operand, wire_vals):
    if operand is None or type(operand) == int:
        return operand
    else:
        return wire_vals[operand]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
