import numpy as np
file = "input07.txt"
with open(file, 'rt') as f:
    lines = f.readlines()

arr = np.empty((len(lines), 2), str)

for i, l in enumerate(lines):
    arr[i, :] = l[5], l[-13]

sor = arr[arr[:, 0].argsort()]
solution = np.empty(1, str)
last = np.unique(arr[:, 1][~np.isin(arr[:, 1], arr[:, 0])])

while sor.size != 0:
    for i, n in enumerate(sor[:, 0]):
        if n not in sor[:, 1]:
            solution = np.append(solution, [n])
            sor = sor[sor[:, 0] != n]
            break

print(''.join(np.append(solution, last)))
