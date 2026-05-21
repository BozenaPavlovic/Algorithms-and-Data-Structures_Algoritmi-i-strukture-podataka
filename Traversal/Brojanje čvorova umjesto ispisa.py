def count_nodes(self, node=None, traversaltype='in'):
    # Ako nije zadan čvor, kreni od korijena
    if node is None:
        node = self.root
    
    # Ako je stablo prazno
    if node is None:
        return 0
    
    # PRE-ORDER: broji korijen, pa lijevo, pa desno
    if traversaltype == 'pre':
        return (1 
                + self.count_nodes(node.left, traversaltype) 
                + self.count_nodes(node.right, traversaltype))
    
    # IN-ORDER: broji lijevo, pa korijen, pa desno
    elif traversaltype == 'in':
        return (self.count_nodes(node.left, traversaltype) 
                + 1 
                + self.count_nodes(node.right, traversaltype))
    
    # POST-ORDER: broji lijevo, pa desno, pa korijen
    elif traversaltype == 'post':
        return (self.count_nodes(node.left, traversaltype) 
                + self.count_nodes(node.right, traversaltype) 
                + 1)
