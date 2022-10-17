def main(raw_input):
    instructions = list(map(lambda x: int(x), raw_input.split('\n')))
    
    jump_count = 0
    pc = 0

    try:
        while True:
            new_pc = pc + instructions[pc]
            if instructions[pc] < 3:
                instructions[pc] += 1
            else:
                instructions[pc] -= 1

            pc = new_pc
            jump_count += 1

    except:
        return jump_count  


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
