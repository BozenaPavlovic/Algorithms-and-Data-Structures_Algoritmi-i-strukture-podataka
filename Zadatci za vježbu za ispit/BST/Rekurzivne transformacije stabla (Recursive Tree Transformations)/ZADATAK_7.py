# U svakom čvoru zamijeniti vrijednost sa 1 ako je dubina čvora parna, 0 ako je neparna 
# (root ima dubinu 0)

def update_depth_parity(node, depth=0):
    if node is None:
        return
    
    original_key = node.key
    
    update_depth_parity(node.left, depth + 1)
    update_depth_parity(node.right, depth + 1)
    
    node.key = 1 if depth % 2 == 0 else 0
    
    return
