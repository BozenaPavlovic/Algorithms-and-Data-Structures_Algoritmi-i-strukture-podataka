class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def delete(self, key):
        parent = None
        current = self.root

        # Find the node to be deleted and its parent
        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return  # Node with key not found

        # Case 1: Node to be deleted has no children (it is a leaf node)
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Case 2: Node to be deleted has two children
        elif current.left and current.right:
            successor = self._min_value_node(current.right)
            val = successor.key
            self.delete(successor.key)
            current.key = val

        # Case 3: Node to be deleted has one child
        else:
            child = current.left if current.left else current.right
            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

    def _min_value_node(self, node): # Returns left-most node
        current = node
        while current.left is not None:
            current = current.left
        return current

# Primjer korištenja
bst = BinarySearchTree()
bst.insert(3)
bst.insert(2)
bst.insert(5)
bst.insert(1)
bst.insert(4)

# Brisanje čvora
bst.delete(3)

# Pretraživanje čvora
result = bst.search(4)
print(f"Čvor pronađen: {result.key}" if result else "Čvor nije pronađen")
