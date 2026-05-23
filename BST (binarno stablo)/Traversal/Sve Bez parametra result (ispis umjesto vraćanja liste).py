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




def pre_order_print(self, node=None):
    if node is None:
        node = self.root
    print(node.key, end=" ")
    if node.left:
        self.pre_order_print(node.left)
    if node.right:
        self.pre_order_print(node.right)

def in_order_print(self, node=None):
    if node is None:
        node = self.root
    if node.left:
        self.in_order_print(node.left)
    print(node.key, end=" ")
    if node.right:
        self.in_order_print(node.right)

def post_order_print(self, node=None):
    if node is None:
        node = self.root
    if node.left:
        self.post_order_print(node.left)
    if node.right:
        self.post_order_print(node.right)
    print(node.key, end=" ")
