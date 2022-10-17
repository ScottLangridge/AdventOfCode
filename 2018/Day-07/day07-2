import time


def main():
    # print('Test:', solve(get_input('example1.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        line = line.strip('\n').split(' ')
        out.append([line[7], line[1], ord(line[7]) - 4])
    return out


def solve(puzzle_input):
    workers = [None] * 5
    # Task = [ID, Dependants, work]
    tasks = {}
    elapsed = 0

    # Generate task dict
    for entry in puzzle_input:
        if entry[0] in tasks.keys():
            tasks[entry[0]][0].append(entry[1])
        else:
            tasks[entry[0]] = [[entry[1]], entry[2]]
    for i in range(65, 91):
        if chr(i) not in tasks.keys():
            tasks[chr(i)] = [[], i - 4]

    # Main loop
    while len(tasks) > 0:
        # Generate ready queue
        ready_queue = []
        for task in tasks.keys():
            if len(tasks[task][0]) == 0:
                ready_queue.append(task)

        # Assign workers
        while worker_free(workers) and len(ready_queue) > 0:
            task_already_assigned = False
            for worker in workers:
                if worker is not None and worker[0] == ready_queue[0]:
                    task_already_assigned = True
                    break
            if not task_already_assigned:
                workers = assign_task(workers, ready_queue[0], tasks)
            del ready_queue[0]

        # Simulate work
        result = run_work(workers)
        workers = result[0]
        elapsed += result[1]

        # Check for completed tasks
        deleted = []
        for worker in workers:
            if worker is not None and worker[1] == 0:
                tasks.pop(worker[0])
                for task in tasks.keys():
                    if worker[0] in tasks[task][0]:
                        tasks[task][0].remove(worker[0])
                deleted.append(worker)
        for d in deleted:
            workers.remove(d)
        for i in range(len(deleted)):
            workers.append(None)

    return elapsed


def run_work(workers):
    elapsed = 0
    task_finished = False
    while not task_finished:
        for worker in workers:
            if worker is not None:
                worker[1] -= 1
                if worker[1] == 0:
                    task_finished = True
        elapsed += 1
    return workers, elapsed


def worker_free(workers):
    for worker_task in workers:
        if worker_task == None:
            return True
    return False


def assign_task(workers, task, tasks):
    i = 0
    while i < len(workers):
        if workers[i] is None:
            workers[i] = [task, tasks[task][1]]
            return workers
        i += 1


def elapse_time(workers, time):
    for i in range(len(workers)):
        workers[i][2] -= time
        if workers[i][2] < 0:
            raise Exception('Elapsed too much time, worker was allowed to idle.')
    return workers


def get_soonest_finsihed(workers):
    soonest = workers[0]
    for task in workers[1:]:
        if task[2] < soonest[2]:
            soonest = [task]
        elif task[2] == soonest[2]:
            soonest.append(task)
    soonest.sort()
    return soonest[0]


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
