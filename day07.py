import numpy as np

file = "input07.txt"
with open(file, 'rt') as f:
    lines = f.readlines()

arr = np.empty((len(lines), 2), str)

for i, l in enumerate(lines):
    arr[i, :] = l[5], l[-13]


rest = np.unique(arr[:, 1][~np.isin(arr[:, 1], arr[:, 0])])
assert len(rest) == 1
last = rest[0]
# add last letter to first column so it is found by get_next_step
arr = np.append(arr, np.array([last, "end"]).reshape(1, 2), axis=0)
sor = arr[arr[:, 0].argsort()]
# Marks if the first letter of the row is in progress (needed for part 2)
in_progress = np.zeros((sor.shape[0], 1), int)
sor = np.append(sor, in_progress, axis=1)


# Part 1


def get_free_steps(sor, num_steps=None):
    not_in_progress = sor[sor[:, 2] != '1']
    if num_steps is None:
        num_steps = not_in_progress.shape[0]
    res = []
    for n in not_in_progress[:, 0]:
        if n not in sor[:, 1]:
            res.append(n)
            num_steps -= 1
            if num_steps < 1:
                return list(set(res))
    return list(set(res))


def solution1(sor):
    sor_copy = np.copy(sor)
    solution = np.empty(0, str)
    while sor_copy.size != 0:
        n = get_free_steps(sor_copy, 1)[0]
        solution = np.append(solution, [n])
        sor_copy = sor_copy[sor_copy[:, 0] != n]
    return solution


print(''.join(solution1(sor)))


# Part 2


def step_time(n):
    return 61 + ord(n) - ord("A")


# This is a generalization of part 1
# Part one can be solved with solution2 with
# free_workers = [1] and free_steps = get_free_steps(sor_copy, 1)
def solution2(sor):
    sor_copy = np.copy(sor)
    time = 0
    free_workers = [1, 2, 3, 4, 5]
    work = {}
    solution = np.empty(0, str)
    while sor_copy.size != 0:
        # try to assign each free worker a free step
        free_steps = get_free_steps(sor_copy)
        while free_steps and free_workers:
            n = free_steps[0]
            free_steps = free_steps[1:]
            # mark rows as "in progress"
            for i, m in enumerate(sor_copy[:, 0]):
                if m == n:
                    sor_copy[i, 2] = '1'
            work[free_workers.pop()] = {"letter": n, "remaining": step_time(n)}
        # if in this step any worker finished, update solution, sor_copy, and bring worker back to free_workers
        work_copy = work.copy() # so we can delete elements of the dictionary during the loop
        for k, v in work_copy.items():
            n = v["letter"]
            v["remaining"] -= 1
            if v["remaining"] == 0:
                free_workers.append(k)
                solution = np.append(solution, [n])
                sor_copy = sor_copy[sor_copy[:, 0] != n]
                work.pop(k)
        time += 1
    return time, solution


time, sol2 = solution2(sor)
print(''.join(sol2))
print(time)
