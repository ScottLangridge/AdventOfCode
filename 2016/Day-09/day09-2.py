def main(raw_input):
    seq = raw_input.strip()
    return count_decompress_len(seq)

def count_decompress_len(seq):
    count = 0

    while seq:
        # Before first marker
        while seq and seq[0] != '(':
            count += 1
            seq = seq[1:]

        # Read marker and count sub_seq
        if seq:
            sub_seq, mult, marker_len = read_marker(seq)
            count += count_decompress_len(sub_seq) * mult
            seq = seq[len(sub_seq) + marker_len:]

    return count




# seq = (NxM)...
def read_marker(seq):
    chars, mult = seq.split(')')[0].strip('(').split('x')
    r = ')'.join(seq.split(')')[1:])[:int(chars)]
    marker_len = len(seq.split(')')[0]) + 1
    return r, int(mult), marker_len


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
