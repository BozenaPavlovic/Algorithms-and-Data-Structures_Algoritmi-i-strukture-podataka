def in_order(self, node=None, result=None):
    if result is None:
        result = []
    if node is None:
        node = self.root
    if node.left is not None:
        self.in_order(node.left, result)
    result.append((node.key, node.value))
    if node.right is not None:
        self.in_order(node.right, result)
    return result
