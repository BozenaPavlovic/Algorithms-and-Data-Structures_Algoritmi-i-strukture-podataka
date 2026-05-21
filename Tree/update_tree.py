class TreeNode: 
  def __init__(self, key): 
    self.key = key 
    self.left = None 
    self.right = None


def update_tree(node):
    if node is None:
        return 0
    
    original_key = node.key
    
    sum_left = update_tree(node.left)
    sum_right = update_tree(node.right)
    
    total_sum = sum_left + sum_right
    
    # Ako je zbroj potomaka paran, postavi vrijednost čvora na 0, inače na 1
    node.key = 0 if total_sum % 2 == 0 else 1
    
    return total_sum + original_key
