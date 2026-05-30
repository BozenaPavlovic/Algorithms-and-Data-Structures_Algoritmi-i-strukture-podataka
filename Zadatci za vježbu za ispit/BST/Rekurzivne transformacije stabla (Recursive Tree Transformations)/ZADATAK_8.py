# U svakom čvoru zamijeniti vrijednost sa prosjekom svih vrijednosti u podstablu 
# (cijeli broj, floor)

def update_average(node):
    if node is None:
        return (0, 0)  # (suma, broj)
    
    original_key = node.key
    
    left_sum, left_count = update_average(node.left)
    right_sum, right_count = update_average(node.right)
    
    total_sum = left_sum + right_sum + original_key
    total_count = left_count + right_count + 1
    
    node.key = total_sum // total_count  # floor prosjek
    
    return (total_sum, total_count)
