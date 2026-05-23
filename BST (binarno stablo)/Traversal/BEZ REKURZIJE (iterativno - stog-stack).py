def pre_order_iterative(self):
    if self.root is None:
        return []
    result = []
    stack = [self.root]
    while stack:
        node = stack.pop()
        result.append(node.key)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def in_order_iterative(self):
    if self.root is None:
        return []
    result = []
    stack = []
    current = self.root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.key)
        current = current.right
    return result

def post_order_iterative(self):
    if self.root is None:
        return []
    result = []
    stack1 = [self.root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        result.append(node.key)
    return result
