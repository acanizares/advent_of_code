from functools import reduce
from itertools import cycle

file = "input01.txt"
with open(file, 'rt') as f:
    lines = f.readlines()


# Part 1
def sum_str(a: str, b: str):
    return int(a) + int(b)


res1 = reduce(sum_str, lines)
print(f"The result is: {res1}")

# Part 2
lines_int = map(lambda x: int(x), lines)
freqs = {0: 1}
freq = 0

for x in cycle(lines_int):
    freq += x
    if freqs.get(freq, None) is not None:
        break
    freqs[freq] = 1

print(f"First repeated frequency: {freq}\n")

