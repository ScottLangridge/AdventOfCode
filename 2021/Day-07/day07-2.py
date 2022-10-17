from tqdm import tqdm

def main(raw_input):
    crab = [int(x) for x in raw_input.split(',')]
    leftmost = min(crab)
    rightmost = max(crab)

    least_fuel = sum(map(lambda i: sum(range(abs(i - 0) + 1)), crab))
    for x in tqdm(range(leftmost, rightmost + 1)):
        fuel = sum(map(lambda i: sum(range(abs(i - x) + 1)), crab))
        if fuel < least_fuel:
            least_fuel = fuel

    return least_fuel


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
