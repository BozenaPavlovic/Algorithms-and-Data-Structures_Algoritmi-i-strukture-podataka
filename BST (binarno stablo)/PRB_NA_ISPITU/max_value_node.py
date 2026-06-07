def max_value_node(self, node):
    current = node
    while current.right is not None:
        current = current.right
    return current