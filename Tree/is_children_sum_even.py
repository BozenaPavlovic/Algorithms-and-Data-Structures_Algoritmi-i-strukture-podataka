def is_children_sum_even(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    
    sum_children = 0
    if node.left:
        sum_children += node.left.key
    if node.right:
        sum_children += node.right.key
    
    if sum_children % 2 != 0:
        return False
    
    return (is_children_sum_even(node.left) and 
            is_children_sum_even(node.right))
