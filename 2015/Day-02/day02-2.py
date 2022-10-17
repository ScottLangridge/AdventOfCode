def main(raw_input):
    boxes = [box.split('x') for box in raw_input.splitlines()]

    ribbon = 0
    for box in boxes:
        l, w, h = [int(dimension) for dimension in box]
        ribbon += wrap_ribbon(l, w, h) + bow_ribbon(l, w, h)

    return ribbon

def wrap_ribbon(l, w, h):
    return min([
        2 * l + 2 * w,
        2 * l + 2 * h,
        2 * w + 2 * h
    ])

def bow_ribbon(l, w, h):
    return l * w * h


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
