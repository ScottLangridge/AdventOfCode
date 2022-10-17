import operator


def main(raw_input):
    expr_sum = 0
    for expr in parse_input(raw_input):
        expr_sum += evaluate_reverse_polish(expr)

    return expr_sum


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    expr_strings = raw_input.splitlines()
    split_exprs = [expr.replace('(', '( ').replace(')', ' )').split(' ') for expr in expr_strings]
    exprs = [list(map(lambda expr: int(expr) if expr.isnumeric() else expr, expr)) for expr in split_exprs]
    return [parse_to_reverse_polish(expr) for expr in exprs]


def parse_to_reverse_polish(expr):
    out = []
    op_stack = []
    for i in expr:
        if isinstance(i, int):
            out.append(i)
        elif i == '+':
            op_stack.append(operator.add)
        elif i == '*':
            while op_stack and op_stack[-1] == operator.add:
                out.append(op_stack.pop())
            op_stack.append(operator.mul)
        elif i == '(':
            op_stack.append('(')
        elif i == ')':
            while op_stack[-1] != '(':
                out.append(op_stack.pop())
            op_stack.pop()
    while op_stack:
        out.append(op_stack.pop())

    return out


def evaluate_reverse_polish(expr):
    val_stack = []
    for i in expr:
        if isinstance(i, int):
            val_stack.append(i)
        else:
            val_stack.append(i(val_stack.pop(), val_stack.pop()))
    return val_stack[0]


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
