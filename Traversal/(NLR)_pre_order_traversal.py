def pre_order_traversal(self, node=None, result=None):
    if result is None:
        result = []
    if node is None:
        node = self.root
    result.append((node.key, node.value))
    if node.left is not None:
        self.pre_order_traversal(node.left, result)
    if node.right is not None:
        self.pre_order_traversal(node.right, result)
    return result
