# U svakom čvoru zamijeniti vrijednost sa visinom njegovog podstabla 
# (visina = max duljina puta do lista)

def update_height(node):
    if node is None:
        return -1  # visina praznog stabla je -1
    
    original_key = node.key
    
    left_height = update_height(node.left)
    right_height = update_height(node.right)
    
    node.key = 1 + max(left_height, right_height)
    
    return 1 + max(left_height, right_height)
