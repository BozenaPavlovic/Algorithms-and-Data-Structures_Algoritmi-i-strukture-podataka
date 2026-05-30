# U svakom čvoru zamijeniti vrijednost sa maksimalnom vrijednošću u njegovom podstablu


def update_max(node):
    if node is None:
        return float('-inf')
    
    original_key = node.key
    
    left_max = update_max(node.left)
    right_max = update_max(node.right)
    
    node.key = max(original_key, left_max, right_max)
    
    return node.key
