def traverse(self, node=None, result=None, traversal_type='in'):
    # Inicijalizacija liste rezultata (samo pri prvom pozivu)
    if result is None:
        result = []
    
    # Ako node nije zadan, kreni od korijena
    if node is None:
        node = self.root
    
    # PRE-ORDER: korijen -> lijevo -> desno
    if traversal_type == 'pre':
        result.append(node.key)
    
    # Rekurzivni poziv za lijevo podstablo
    if node.left:
        self.traverse(node.left, result, traversal_type)
    
    # IN-ORDER: lijevo -> korijen -> desno
    if traversal_type == 'in':
        result.append(node.key)
    
    # Rekurzivni poziv za desno podstablo
    if node.right:
        self.traverse(node.right, result, traversal_type)
    
    # POST-ORDER: lijevo -> desno -> korijen
    if traversal_type == 'post':
        result.append(node.key)
    
    return result
