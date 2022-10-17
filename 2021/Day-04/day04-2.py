class BingoCard:
    def __init__(self, input_string):
        split_rows = [row.split() for row in input_string.splitlines()]

        self.row_count = len(split_rows)
        self.col_count = len(split_rows[0])

        self.nums = {}
        self.num_grid = []
        self.called_grid = []
        for y, row in enumerate(split_rows):
            self.num_grid.append([])
            self.called_grid.append([False for x in row])
            for x, num in enumerate(row):
                self.nums[int(num)] = (x, y)
                self.num_grid[-1].append(int(num))

    def call_num(self, num):
        if num in self.nums.keys():
            x, y = self.nums[num]
            self.called_grid[y][x] = True

    def has_bingo(self):
        # Check rows
        for y in range(self.row_count):
            if sum(self.called_grid[y]) == 5:
                return True

        # Check cols
        for x in range(self.col_count):
            if sum([row[x] for row in self.called_grid]) == 5:
                return True

    def score(self, last_called):
        score = 0
        for y in range(self.row_count):
            for x in range(self.col_count):
                if not self.called_grid[y][x]:
                    score += self.num_grid[y][x]
        return score * last_called


def main(raw_input):
    input_blocks = raw_input.split('\n\n')
    called_nums = [int(x) for x in input_blocks[0].split(',')]
    cards = [BingoCard(x) for x in input_blocks[1:]]

    for num in called_nums:
        i = 0
        while i < len(cards):
            card = cards[i]
            card.call_num(num)
            if card.has_bingo():
                if len(cards) > 1:
                    cards.remove(card)
                    i -= 1
                else:
                    return card.score(num)
            i += 1

    return False


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
