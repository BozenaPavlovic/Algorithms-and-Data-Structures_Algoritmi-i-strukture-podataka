def post_order_traversal(self, node=None, result=None):
    if result is None:
        result = []
    if node is None:
        node = self.root
    if node.left is not None:
        self.post_order_traversal(node.left, result)
    if node.right is not None:
        self.post_order_traversal(node.right, result)
    result.append((node.key, node.value))
    return result
