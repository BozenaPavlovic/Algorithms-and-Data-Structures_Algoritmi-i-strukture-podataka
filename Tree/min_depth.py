def min_depth(node):
    if not node:
        return 0
    if not node.left:
        return 1 + min_depth(node.right)
    if not node.right:
        return 1 + min_depth(node.left)
    return 1 + min(min_depth(node.left), min_depth(node.right))
