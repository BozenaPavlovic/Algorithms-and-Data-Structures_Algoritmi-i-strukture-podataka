def traverse(self, node=None, traversaltype='in'):
    if node is None:
        node = self.root
    
    if traversaltype == 'pre':
        print(node.key, end=' ')
        if node.left: self.traverse(node.left, traversaltype)
        if node.right: self.traverse(node.right, traversaltype)
    elif traversaltype == 'in':
        if node.left: self.traverse(node.left, traversaltype)
        print(node.key, end=' ')
        if node.right: self.traverse(node.right, traversaltype)
    elif traversaltype == 'post':
        if node.left: self.traverse(node.left, traversaltype)
        if node.right: self.traverse(node.right, traversaltype)
        print(node.key, end=' ')



# TEST
bst = BST()
for broj in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(broj)

print("In-order: ", end='')
bst.traverse_print(traversal_type='in')     # Ispis: 20 30 40 50 60 70 80
print("\nPre-order: ", end='')
bst.traverse_print(traversal_type='pre')    # Ispis: 50 30 20 40 70 60 80
print("\nPost-order: ", end='')
bst.traverse_print(traversal_type='post')   # Ispis: 20 40 30 60 80 70 50
