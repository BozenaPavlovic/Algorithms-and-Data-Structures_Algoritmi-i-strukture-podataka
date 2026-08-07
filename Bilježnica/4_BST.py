#%%
class TreeNodeDict:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTDict:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = TreeNodeDict(key, value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                # key exists -> update value
                current.value = value
                break

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

        # Case 1: Node to be deleted has no children (leaf)
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
            return

        # Case 2: Node to be deleted has two children
        if current.left is not None and current.right is not None:
            successor = self._min_value_node(current.right)
            succ_key, succ_value = successor.key, successor.value
            # delete successor (will remove that node)
            self.delete(successor.key)
            # copy successor's key and value into current
            current.key = succ_key
            current.value = succ_value
            return

        # Case 3: Node to be deleted has one child
        child = current.left if current.left else current.right
        if current != self.root:
            if current == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            self.root = child
        return

    def _min_value_node(self, node):  # Returns left-most node
        current = node
        while current.left is not None:
            current = current.left
        return current

