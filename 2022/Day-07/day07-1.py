class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def get_size(self):
        return sum(map(lambda i: i.get_size(), self.children))


class File:
    def __init__(self, str_file):
        size, self.name = str_file.split()
        self.size = int(size)

    def get_size(self):
        return self.size


def main(raw_input):
    terminal = raw_input.splitlines()[1:]
    root = Dir("/", None)

    current_dir = root
    all_dirs = [root]
    for row in terminal:
        if row == "$ cd ..":
            current_dir = current_dir.parent
        elif row.startswith("$ cd"):
            new_dir = Dir(row.split()[-1], current_dir)
            all_dirs.append(new_dir)
            current_dir.children.append(new_dir)
            current_dir = new_dir
        elif row[0].isdigit():
            current_dir.children.append(File(row))

    sum_size = 0
    for i in all_dirs:
        size = i.get_size()
        if size <= 100000:
            sum_size += size

    return sum_size


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
