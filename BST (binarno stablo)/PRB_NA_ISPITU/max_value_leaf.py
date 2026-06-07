def max_value_leaf(self, node):
    if node is None:
        return None
    current = node
    while current.left is not None or current.right is not None:
        if current.right is not None:
            current = current.right
        else:
            current = current.left
    return current.key