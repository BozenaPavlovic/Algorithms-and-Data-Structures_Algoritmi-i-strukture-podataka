# U svakom čvoru zamijeniti vrijednost sa brojem čvorova u njegovom podstablu 
# (uključujući njega samog)


def count_nodes(node):
    if node is None:
        return 0
    
    original_key = node.key
    
    left_count = count_nodes(node.left)
    right_count = count_nodes(node.right)
    
    node.key = 1 + left_count + right_count
    
    return 1 + left_count + right_count
