def main(raw_input):
    raw_input = list(raw_input)
    raw_input.insert(0, raw_input[-1])
    
    sum = 0
    for i in range(len(raw_input) - 1):
        if raw_input[i] == raw_input[i + 1]:
            sum += int(raw_input[i])

    return sum

def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
