def set_depth(node, depth=0):
    if node is None:
        return
    node.key = depth
    set_depth(node.left, depth + 1)
    set_depth(node.right, depth + 1)
