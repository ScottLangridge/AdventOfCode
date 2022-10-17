import time
from collections import defaultdict
from random import shuffle


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    log = parse_input(puzzle_input)
    guards = defaultdict(lambda: 0)
    current_guard = None
    sleep_start = None

    # Calculate sleep time for each guard
    for record in log:
        action = record[1]
        datetime = record[0]
        if action[0] == 'G':
            current_guard = guard_change_get_id(record)
        if action == 'falls asleep':
            sleep_start = datetime[-5:]
        if action == 'wakes up':
            sleep_end = datetime[-5:]
            guards[current_guard] += time_between(sleep_start, sleep_end)

    # Get guard that sleeps most
    sleepiest_guard = None
    sleep_time_of_sleepiest_guard = 0
    for guard_id in guards.keys():
        if guards[guard_id] > sleep_time_of_sleepiest_guard:
            sleepiest_guard = guard_id
            sleep_time_of_sleepiest_guard = guards[guard_id]

    # Extract just his information from log
    pointer = 0
    while pointer != len(log):
        if guard_change_get_id(log[pointer]) == sleepiest_guard:
            del log[pointer]
            while pointer != len(log) and (not is_guard_change(log[pointer])):
                pointer += 1
        else:
            del log[pointer]
            while pointer != len(log) and (not is_guard_change(log[pointer])):
                del log[pointer]

    # The length of the log should be even since a guard should always wake up after sleeping.
    assert (len(log) % 2 == 0)

    # Set up sleep log [(sleeptime: waketime), (sleeptime:waketime) ... ]
    sleep_log = []
    for i in range(0, len(log), 2):
        sleep_log.append((int(log[i][0][-2:]), int(log[i + 1][0][-2:]) - 1))

    sleep_count_by_min = defaultdict(lambda: 0)
    for sleep in sleep_log:
        i = sleep[0]
        while i <= sleep[1]:
            sleep_count_by_min[i] += 1
            i += 1

    longest_sleep = 0
    sleepiest_min = None
    for minute in sleep_count_by_min.keys():
        if sleep_count_by_min[minute] > longest_sleep:
            sleepiest_min = minute
            longest_sleep = sleep_count_by_min[minute]

    return int(sleepiest_guard) * sleepiest_min


def is_guard_change(record):
    if '#' in record[1]:
        return True
    else:
        return False


def guard_change_get_id(record):
    return record[1].split(' ')[1][1:]


def time_between(start, end):
    start = start.split(':')
    end = end.split(':')
    start[0] = int(start[0])
    start[1] = int(start[1])
    end[0] = int(end[0])
    end[1] = int(end[1])

    diff = 0
    while start[0] != end[0]:
        start[0] = (1 + start[0]) % 24
        diff += 60

    diff += end[1] - start[1]
    return diff


def parse_input(puzzle_input):
    records = []
    for line in puzzle_input:
        # Split into datetime and string
        line = line[1:]
        split_line = line.split('] ')
        records.append([split_line[0], split_line[1]])
    records.sort()
    return records


def scramble_example():
    with open('example1.txt', 'r') as f:
        lines = f.readlines()
        shuffle(lines)
    with open('rand_example1.txt', 'w') as f:
        f.writelines(lines)


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
