# U svakom čvoru zamijeniti vrijednost sa 1 ako je produkt potomaka paran, 0 ako je neparan

def update_product_parity(node):
    if node is None:
        return 1  # neutralni element za množenje
    
    original_key = node.key
    
    left_prod = update_product_parity(node.left)
    right_prod = update_product_parity(node.right)
    
    total_product = left_prod * right_prod
    
    node.key = 0 if total_product % 2 == 0 else 1
    
    return total_product * original_key
