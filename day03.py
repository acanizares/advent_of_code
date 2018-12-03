from typing import Tuple
import numpy as np
import sys

file = "input03.txt"
with open(file, 'rt') as f:
    lines = f.readlines()


def parse_input(input: str) -> Tuple[int, int, int, int]:
    """Transform the input string into x, y, w, h"""
    head, tail = input.split("@ ")
    points, measures = tail.split(": ")
    x, y = points.split(",")
    w, h = measures.split("x")
    return int(x), int(y), int(w), int(h)

parsed_inputs = list(map(parse_input, lines))

# Part 1

d = 1100
m = np.zeros((d, d), int)  # d*d matrix of zeros

for x, y, w, h in parsed_inputs:
    sub_m = np.ones((w, h), int)
    full_m = np.pad(sub_m, ((x, d - (x + w)), (y, d - (y + h))), mode='constant')
    m += full_m

mask = m >= 2
overlap = np.count_nonzero(mask)

print(f"Total overlap: {overlap}")

# Part 2

sys.setrecursionlimit(1500)

def intersection(a: int, b: int, c: int, d: int):
    """Measure of (a, b) intersected with (c, d)."""
    assert a <= b and c <= d
    return max(0, min(b, d) - max(a, c))


def intersection_inputs(n, m):
    nx, ny, nw, nh = n
    mx, my, mw, mh = m
    return intersection(nx, nx+nw, mx, mx+mw)*intersection(ny, ny+nh, my, my+mh)


def is_disjoint(x, xs):
    if not xs:
        return True
    return intersection_inputs(x, xs[0]) == 0 and is_disjoint(x, xs[1:])


def find_disjoint(parsed_inputs):
    for i, n in enumerate(parsed_inputs):
        found = is_disjoint(n, parsed_inputs[:i]) and is_disjoint(n, parsed_inputs[i+1:])
        if found:
            return i+1
    raise ValueError("No disjoint element was found.")

print(f"Id of the disjoint element: {find_disjoint(parsed_inputs)}")
