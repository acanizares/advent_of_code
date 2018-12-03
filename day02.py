from typing import List

file = "input02.txt"

with open(file, "rt") as f:
    ids = f.readlines()

# Part 1

doubles = 0
triples = 0

for id in ids:
    double_found = False
    triple_found = False
    for c in id:
        reps = id.count(c)
        if reps == 2 and not double_found:
            doubles += 1
            double_found = True
        if reps == 3 and not triple_found:
            triples += 1
            triple_found = True
        if double_found and triple_found:
            break

print(f"Number of doubles: {doubles}")
print(f"Number of triples: {triples}")
print(f"Checksum: {doubles*triples}")

# Part 2


def check(x: str, y: str) -> bool:
    """
    Whether two strings differ at most at one position
    """
    if not x:
        return not y
    x0, x_tail = x[0], x[1:]
    y0, y_tail = y[0], y[1:]
    return (x_tail == y_tail) or (x0 == y0 and check(x_tail, y_tail))


def find_ids(ids: List[str]) -> str:
    for i, x in enumerate(ids[:-1]):
        for y in ids[i + 1:]:
            found = check(x, y)
            if found:
                print(f"The found ids: {x}, {y}")
                common_sub = ""
                for i, c in enumerate(x):
                    if y[i] == c:
                        common_sub += c
                return(common_sub)
    raise ValueError("No correct ids were found")


res = find_ids(ids)
print(f"The common substring: {res}")
