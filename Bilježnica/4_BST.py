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
        """Ako ključ postoji -> update value; inače umetni novi čvor."""
        if self.root is None:
            self.root = TreeNodeDict(key, value)
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = TreeNodeDict(key, value)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = TreeNodeDict(key, value)
                    return
                current = current.right
            else:  # key == current.key -> update vrijednost
                current.value = value
                return

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

    def delete(self, key):
        """Obriši čvor s danim ključem; ako ne postoji, ne radi ništa."""
        parent = None
        current = self.root

        # Pronađi čvor i parenta
        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return  # ključ nije pronađen

        # Case 1: list
        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            else:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            return

        # Case 2: dva djeteta
        if current.left is not None and current.right is not None:
            successor = self._min_value_node(current.right)
            succ_key, succ_value = successor.key, successor.value
            # obriši successor (on će biti leaf ili imati najviše jedno dijete)
            self.delete(successor.key)
            # kopiraj key i value successor-a u current
            current.key = succ_key
            current.value = succ_value
            return

        # Case 3: jedno dijete
        child = current.left if current.left is not None else current.right
        if parent is None:
            self.root = child
        else:
            if parent.left == current:
                parent.left = child
            else:
                parent.right = child
        return

    def _min_value_node(self, node):
        """Pomoćna: vrati najmanji (lijevi-most) node u podstablu."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def in_order_traversal(self, node=None, result=None):
        """Rekurzivno in-order: vraća listu (key, value) tupleova sortiranu po ključu."""
        if result is None:
            result = []
        if node is None:
            node = self.root
        def _in(n):
            if n is None:
                return
            _in(n.left)
            result.append((n.key, n.value))
            _in(n.right)
        _in(node)
        return result
