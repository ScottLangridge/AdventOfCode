import time
from collections import defaultdict
from random import shuffle


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    log = parse_input(puzzle_input)

    # Create list of guard IDs
    guard_sleep_logs = {}
    for record in log:
        action = record[1]
        if action[0] == 'G':
            guard_sleep_logs[guard_change_get_id(record)] = None

    # For each guard
    for guard_id in guard_sleep_logs.keys():
        # Extract just his info from the log to make a personal log for him
        log_copy = log[:]
        pointer = 0
        while pointer != len(log_copy):
            if guard_change_get_id(log_copy[pointer]) == guard_id:
                del log_copy[pointer]
                while pointer != len(log_copy) and (not is_guard_change(log_copy[pointer])):
                    pointer += 1
            else:
                del log_copy[pointer]
                while pointer != len(log_copy) and (not is_guard_change(log_copy[pointer])):
                    del log_copy[pointer]

        # Set up sleep log to store minutes only and save it to guard
        sleep_log = []
        for i in range(0, len(log_copy), 2):
            sleep_log.append((int(log_copy[i][0][-2:]), int(log_copy[i + 1][0][-2:]) - 1))
        guard_sleep_logs[guard_id] = sleep_log

    # Count sleepiest min for each guard
    most_slept = None
    most_slept_frequency = 0
    for guard_id in guard_sleep_logs.keys():
        times_slept_on_a_given_min = defaultdict(lambda: 0)
        for sleep in guard_sleep_logs[guard_id]:
            i = sleep[0]
            while i <= sleep[1]:
                times_slept_on_a_given_min[i] += 1
                i += 1

        for minute in times_slept_on_a_given_min.keys():
            if times_slept_on_a_given_min[minute] > most_slept_frequency:
                most_slept = (int(guard_id), minute)
                most_slept_frequency = times_slept_on_a_given_min[minute]

    return most_slept[0] * most_slept[1]


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
