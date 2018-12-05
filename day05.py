import re

file = "input05.txt"
with open(file, 'rt') as f:
    lines = f.readlines()

assert len(lines) == 1
polymer = lines[0]
polymer = polymer.replace("\n", "")

def will_react(x, y):
    if abs(ord(x) - ord (y)) == 32:
        return True
    else:
        return False

def react(polymer):
    aux = polymer
    i = 0
    while i < len(aux) - 1:
        head, tail = aux[:i], aux[i + 2:]
        x, y = aux[i], aux[i + 1]
        if will_react(x, y):
            aux = head + tail
            i = max(0, i - 1)  # go one step back to find rew reactions
        else:
            i += 1
    return aux

# Part 1
remaining = react(polymer)
print(f"Remaining units: {len(remaining)}")


# Part 2

results = {}
for ord_c in range(ord('a'), ord('z') + 1):
    c = chr(ord_c)
    polymer_no_c = re.sub(c, "", polymer, flags=re.IGNORECASE)
    results[c] = len(react(polymer_no_c))

worst_letter = min(results, key=results.get)
print(f"The worst letter is: {worst_letter}")
print(f"The length of the shortest polymer is: {results[worst_letter]}")
print(results)
