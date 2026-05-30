# U svakom čvoru zamijeniti vrijednost sa 0 ako je broj potomaka paran, 1 ako je neparan

def update_parity(node):
    if node is None:
        return 0
    
    original_key = node.key
    
    left_count = update_parity(node.left)
    right_count = update_parity(node.right)
    
    total_descendants = left_count + right_count
    
    node.key = 0 if total_descendants % 2 == 0 else 1
    
    return total_descendants + 1  # +1 za trenutni čvor
