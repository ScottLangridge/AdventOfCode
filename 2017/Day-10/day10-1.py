def main(raw_input):
    lst = range(0, 256)
    current_pos = 0
    skip_size = 0
    lenghts = [int(x) for x in raw_input.split(',')]
    
    return None


def split_list(start, length):
    

def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('Day-10\input.txt')
    print(main(puzzle_input))
