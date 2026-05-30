# U svakom čvoru zamijeniti vrijednost sa minimalnom vrijednošću u njegovom podstablu

def update_min(node):
    if node is None:
        return float('inf')
    
    original_key = node.key
    
    left_min = update_min(node.left)
    right_min = update_min(node.right)
    
    node.key = min(original_key, left_min, right_min)
    
    return node.key
