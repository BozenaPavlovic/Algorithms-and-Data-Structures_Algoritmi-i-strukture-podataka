# U svakom čvoru zamijeniti vrijednost sa zbrojem svih listova u njegovom podstablu 
# (list = čvor bez djece)



def sum_leaves(node):
    if node is None:
        return 0
    
    original_key = node.key
    
    left_sum = sum_leaves(node.left)
    right_sum = sum_leaves(node.right)
    
    # Ako je list (nema djece), onda je sam svoj list
    if node.left is None and node.right is None:
        node.key = 1  # sam je list
        return 1
    else:
        node.key = left_sum + right_sum
        return left_sum + right_sum
