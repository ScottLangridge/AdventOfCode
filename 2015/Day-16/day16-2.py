class Aunt:
    def __init__(self, def_string):
        self.num = None
        self.info = {}
        self.parse_definition(def_string)
        self.known_info = self.info.keys()

    def parse_definition(self, def_string):
        tokens = def_string.split()
        self.num = int(tokens[1].strip(':'))
        self.info = {}
        for i in range(2, len(tokens), 2):
            k = tokens[i].strip(':')
            v = int(tokens[i + 1].strip(','))
            self.info[k] = v

    def matches_dict(self, facts):
        for k, v in facts.items():
            if not self._matches(k, v):
                return False
        return True

    def _matches(self, key, val):
        if key not in self.known_info:
            return True
        else:
            if key in ['cats', 'trees']:
                return self.info[key] > val
            elif key in ['pomeranians', 'goldfish']:
                return self.info[key] < val
            else:
                return self.info[key] == val


def main(raw_input):
    aunts = [Aunt(aunt_def) for aunt_def in raw_input.splitlines()]
    facts = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }
    return next(filter(lambda x: x.matches_dict(facts), aunts)).num


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
