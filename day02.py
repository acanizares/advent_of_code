file = "input02.txt"

with open(file, "rt") as f:
    ids = f.readlines()


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
