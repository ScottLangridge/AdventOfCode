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

    # Find layer with least 0s
    min_zero_layer = layers[0]
    min_zero_count = layers[0].count(0)
    for layer in layers[1:]:
        if layer.count(0) < min_zero_count:
            min_zero_layer = layer
            min_zero_count = layer.count(0)

    # Generate output
    ones = min_zero_layer.count(1)
    twos = min_zero_layer.count(2)
    val = ones * twos

    return val


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return list(raw_input)


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
