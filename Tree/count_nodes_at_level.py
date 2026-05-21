def count_nodes_at_level(node, target_level, current_level=0):
    if not node:
        return 0
    if current_level == target_level:
        return 1
    return (count_nodes_at_level(node.left, target_level, current_level + 1) +
            count_nodes_at_level(node.right, target_level, current_level + 1))
