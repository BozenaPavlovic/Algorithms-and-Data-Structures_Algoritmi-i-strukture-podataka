def level_order(self):
    if self.root is None:
        return []

    result = []
    queue = [self.root]  # koristimo listu kao red

    while queue:
        node = queue.pop(0)  # uzmi prvog u redu (FIFO)
        result.append(node.key)

        if node.left:
            queue.append(node.left)  # lijevo dijete na kraj reda
        if node.right:
            queue.append(node.right)  # desno dijete na kraj reda

    return result