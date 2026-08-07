class TreeNodeDict:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTDict:
    def __init__(self):
        self.root = None

    def search(self, key):
        """Vrati node ako postoji, inače None."""
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def get(self, key):
        node = self.search(key)
        return node.value if node else None

    def insert(self, key, value):
        """Ako ključ postoji -> update value; inače ubaci novi čvor."""
        new_node = TreeNodeDict(key, value)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:  # key == current.key -> update value
                current.value = value
                return

    def delete(self, key):
        """Obriši node s danim ključem. Ako ne postoji, radi ništa."""
        parent = None
        current = self.root

        # pronađi čvor i parenta
        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return  # nije pronađen

        # Case 1: leaf
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Case 2: dva djeteta
        elif current.left and current.right:
            successor = self._min_value_node(current.right)
            # kopiraj key i value successor-a u current
            succ_key, succ_value = successor.key, successor.value
            # obriši successor (privremeno koristi delete rekurzivno)
            self.delete(successor.key)
            current.key = succ_key
            current.value = succ_value

        # Case 3: jedno dijete
        else:
            child = current.left if current.left else current.right
            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

 
