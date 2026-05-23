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


# TEST
bst = BST()
for broj in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(broj)

print("Broj čvorova (pre):", bst.count_nodes(traversal_type='pre'))   # 7
print("Broj čvorova (in):", bst.count_nodes(traversal_type='in'))     # 7
print("Broj čvorova (post):", bst.count_nodes(traversal_type='post')) # 7
