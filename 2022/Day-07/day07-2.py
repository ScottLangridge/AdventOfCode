class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = None

    def get_size(self):
        if self.size is None:
            self.size = sum(map(lambda i: i.get_size(), self.children))
        return self.size


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

    unused = 70000000 - root.get_size()
    must_clear = 30000000 - unused
    for i in sorted(all_dirs, key=lambda d: d.get_size()):
        if i.get_size() >= must_clear:
            return i.get_size()


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
