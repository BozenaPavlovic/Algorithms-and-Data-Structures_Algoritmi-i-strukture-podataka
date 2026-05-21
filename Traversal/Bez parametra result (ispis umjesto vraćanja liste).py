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
