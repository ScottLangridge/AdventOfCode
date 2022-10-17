def main(raw_input):
    data = [int(val) for val in parse_input(raw_input)]
    dimensions = (25, 6)
    pixel_count = dimensions[0] * dimensions[1]

    # Build layers
    layers = []
    input_pointer = 0
    while input_pointer < len(data):
        current_layer = []
        for _ in range(pixel_count):
            current_layer.append(data[input_pointer])
            input_pointer += 1
        layers.append(current_layer)

    # Generate combined image
    final_layer = list(zip(*layers))
    for i in range(len(final_layer)):
        final_layer[i] = get_visible(final_layer[i])

    pretty_print_layer(dimensions, final_layer)
    return ''.join([str(i) for i in final_layer])


def get_visible(pix_stack):
    for pix in pix_stack:
        if pix != 2:
            return pix


def pretty_print_layer(dimensions, layer):
    b = ' '
    w = '#'
    t = ' '
    colours = {0: b, 1: w, 2: t}

    i = 0
    for y in range(dimensions[1]):
        line = ''
        for x in range(dimensions[0]):
            line = line + colours[layer[i]]
            i += 1
        print(line)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return list(raw_input)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
