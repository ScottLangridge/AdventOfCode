def main(raw_input):
    data = parse_input(raw_input)
    wire1 = gen_wiremap(data[0])
    wire2 = gen_wiremap(data[1])

    intersections = get_intersections(wire1, wire2)
    manhattens = []
    for i in intersections:
        manhattens.append(abs(i[0]) + abs(i[1]))

    return min(manhattens)


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    wires = raw_input.split('\n')
    return [wires[0].split(','), wires[1].split(',')]


def gen_wiremap(wire):
    x = 0
    y = 0
    wiremap = []
    for input_line in wire:
        line = {}
        if input_line[0] == 'R':
            line['direction'] = 'x'
            line['constant'] = y
            line['start'] = x + 1
            line['end'] = x + int(input_line[1:])
            x = line['end']

        elif input_line[0] == 'L':
            line['direction'] = 'x'
            line['constant'] = y
            line['start'] = x - 1
            line['end'] = x - int(input_line[1:])
            x = line['end']
        elif input_line[0] == 'U':
            line['direction'] = 'y'
            line['constant'] = x
            line['start'] = y + 1
            line['end'] = y + int(input_line[1:])
            y = line['end']
        else:
            line['direction'] = 'y'
            line['constant'] = x
            line['start'] = y - 1
            line['end'] = y - int(input_line[1:])
            y = line['end']
        wiremap.append(line)

    return wiremap


def get_intersections(wire1, wire2):
    intersections = []
    for line1 in wire1:
        for line2 in wire2:
            if line1['direction'] == line2['direction']:
                if line1['constant'] == line2['constant']:
                    if in_plane_lines_intersect(line1, line2):
                        for i in range(line1['start'], line1['end'] + 1):
                            if i in range(line2['start'], line2['end'] + 1):
                                intersections.append((line1['constant'], i))
            else:
                if perpendicular_lines_intersect(line1, line2):
                    if line1['direction'] == 'x':
                        intersections.append((line2['constant'], line1['constant']))
                    else:
                        intersections.append((line1['constant'], line2['constant']))
    return intersections


def in_plane_lines_intersect(line1, line2):
    return line1['start'] < line2['start'] < line1['end'] \
           or line2['start'] < line1['start'] < line2['end']


def perpendicular_lines_intersect(line1, line2):
    return (line1['start'] < line2['constant'] < line1['end'] and line2['start'] < line1['constant'] < line2['end']) or \
           (line1['start'] > line2['constant'] > line1['end'] and line2['start'] < line1['constant'] < line2['end']) or \
           (line1['start'] < line2['constant'] < line1['end'] and line2['start'] > line1['constant'] > line2['end']) or \
           (line1['start'] > line2['constant'] > line1['end'] and line2['start'] > line1['constant'] > line2['end'])


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
