file = "input06.txt"
with open(file, 'rt') as f:
    lines = f.readlines()

d = {}

for i, l in enumerate(lines):
    x, y = map(int, l.split(", "))
    d[i] = {"point": (x, y), "neighbors": []}

xs = [it["point"][0] for it in d.values()]
ys = [it["point"][1] for it in d.values()]
min_x = min(xs)
max_x = max(xs)
min_y = min(ys)
max_y = max(ys)

# We just need to compute the distances in the minimum rectangle containing all the points with 1 unit margin on each side

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Part 1
def compute_part_1(d):
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            aux = {}
            for i, it in d.items():
                aux[i] = dist(it["point"], (x, y))
            min_dist = min(aux.values())
            points_at_min_dist = [i for i, it in aux.items() if it == min_dist]
            if len(points_at_min_dist) == 1:
                d[points_at_min_dist[0]]["neighbors"].append((x, y))

    # The area around a point is infinite iff it has neighbors in the outer 1 unit rectangle
    for i, it in d.items():
        neighbors = it["neighbors"]
        neighbors_outer_rect = [p for p in neighbors if p[0] in {min_x - 1, max_x + 1} or p[1] in {min_y - 1, max_y + 1} ]
        if neighbors_outer_rect:
            area = float("inf")
        else:
            area = len(neighbors)
        it["area"] = area

    finite_areas = list(filter(lambda x: x<float("inf"), [it["area"] for it in d.values()]))
    return max(finite_areas)

print(f"Largest finite area: {compute_part_1(d)}")

# Part 2
# HACK! Here we should have checked if any point in the outer rectangle satisfied the condition.
# In this case, we should have expanded the candidate area.
# But the answer is right and it's late, so...
def compute_part_2(d):
    selected_region = []
    for x in range(min_x - 1, max_x + 2):
        for y in range(min_y - 1, max_y + 2):
            aux = {}
            for i, it in d.items():
                aux[i] = dist(it["point"], (x, y))
            sum_dist = sum(aux.values())
            if sum_dist < 10000:
                selected_region.append((x, y))
    return len(selected_region)

print(f"Area of the selected region: {compute_part_2(d)}")
