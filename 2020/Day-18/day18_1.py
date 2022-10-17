import operator


def main(raw_input):
    expressions_sum = 0
    for expression in parse_input(raw_input):
        expressions_sum += evaluate_expression(expression)

    return expressions_sum


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    expr_strings = raw_input.splitlines()
    split_exprs = [expr.replace('(', '( ').replace(')', ' )').split(' ') for expr in expr_strings]
    return [list(map(lambda expr: int(expr) if expr.isnumeric() else expr, expr)) for expr in split_exprs]


def evaluate_expression(expr):
    out = 0
    op = operator.add
    i = 0
    while i < len(expr):
        if expr[i] == '+':
            op = operator.add
        elif expr[i] == '*':
            op = operator.mul
        elif expr[i] == '(':
            sub_expr = []
            bracket_depth = 0
            i += 1
            while not (expr[i] == ')' and bracket_depth == 0):
                sub_expr.append(expr[i])
                if expr[i] == '(':
                    bracket_depth += 1
                elif expr[i] == ')':
                    bracket_depth -= 1
                i += 1

            out = op(out, evaluate_expression(sub_expr))
        else:
            out = op(out, expr[i])

        i += 1

    return out


def get_first_operation(expr):
    i = 1
    bracket_depth = 0
    while True:
        if expr[i] == '+':
            return operator.add
        elif expr[i] == '*':
            return operator.mul
        elif expr[i] == '(':
            while not (expr[i] == ')' and bracket_depth == 0):
                i += 1
                if expr[i] == '(':
                    bracket_depth += 1
                elif expr[i] == ')':
                    bracket_depth -= 1


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
