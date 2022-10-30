def main(raw_input):
    seq = list(raw_input.strip())
    return len(decompress(seq))


def decompress(seq):
    out = ""
    while seq:
        c = seq.pop(0)

        # If the start of a marker
        if c == '(':
            # Build whole marker
            str_marker = ''
            while True:
                c = seq.pop(0)
                if c == ')':
                    break
                else:
                    str_marker += c

            marker = [int(i) for i in str_marker.split('x')]

            # Get marked text
            str_copy = ''.join(seq[:marker[0]])
            seq = seq[marker[0]:]

            # Repeat marked text
            for i in range(marker[1]):
                out += str_copy

        else:
            out += c

    return out


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
