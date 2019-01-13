file = "input08.txt"
with open(file, 'rt') as f:
    lines = f.readlines()
assert len(lines) == 1
numbers = list(map(int, lines[0].split()))


class Node(list):
    metadata: list

    def __init__(self):
        self.metadata = []
        super().__init__()

    def add_metadata(self, metadata):
        self.metadata.extend(metadata)


def process(numbers: str, node: Node, acc: int=0):
    if not numbers:
        return numbers, node, acc
    elif len(numbers) < 2:
        raise ValueError("Input is too short.")
    else:
        n_children, n_meta = numbers[:2]
        rest_numbers = numbers[2:]
        for _ in range(n_children):
            rest_numbers, child_node, acc = process(rest_numbers, node, acc)
            node.append(child_node)
        metadata, rest_numbers = rest_numbers[:n_meta], rest_numbers[n_meta:]
        node.add_metadata(metadata)
        acc += sum(metadata)
        return rest_numbers, node, acc


root = Node()
print(f"Metadata sum: {process(numbers, root)[2]}")
