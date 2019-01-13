file = "input08.txt"
with open(file, 'rt') as f:
    lines = f.readlines()
assert len(lines) == 1
numbers = list(map(int, lines[0].split()))


class Node(list):
    metadata: list
    value: int

    def __init__(self):
        self.metadata = []
        self.value = 0
        super().__init__()

    def add_metadata(self, metadata):
        self.metadata.extend(metadata)

    def update_value(self):
        self.value = 0
        if not self:  # if node has no children
            self.value = sum(self.metadata)
        for m in self.metadata:
            extra_value = 0
            try:
                child = self[m-1]
            except IndexError:
                pass
            else:
                child.update_value()
                extra_value = child.value
            self.value += extra_value


def process(numbers: str, node: Node, acc: int=0):
    if not numbers:
        return numbers, node, acc
    elif len(numbers) < 2:
        raise ValueError("Input is too short.")
    else:
        n_children, n_meta = numbers[:2]
        rest_numbers = numbers[2:]
        for _ in range(n_children):
            rest_numbers, child_node, acc = process(rest_numbers, Node(), acc)
            node.append(child_node)
        metadata, rest_numbers = rest_numbers[:n_meta], rest_numbers[n_meta:]
        node.add_metadata(metadata)
        acc += sum(metadata)
        return rest_numbers, node, acc


root = Node()
print(f"Metadata sum: {process(numbers, root)[2]}")
root.update_value()
print(f"Value of root: {root.value}")
