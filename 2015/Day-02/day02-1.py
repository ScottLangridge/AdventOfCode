def main(raw_input):
    boxes = [box.split('x') for box in raw_input.splitlines()]

    wrapping_paper = 0
    for box in boxes:
        l, w, h = [int(dimension) for dimension in box]
        wrapping_paper += surface_area(l, w, h) + slack(l, w, h)

    return wrapping_paper


def surface_area(l, w, h):
    return (2 * l * w) + (2 * w * h) + (2 * h * l)


def slack(l, w, h):
    return min([l * w, w * h, h * l])


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
