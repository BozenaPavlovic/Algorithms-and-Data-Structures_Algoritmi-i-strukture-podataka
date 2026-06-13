# Mapa / rječnik temeljen na BST-u

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
                current.value = value
                break

    def search(self, key):
        current = self.root

        while current is not None:
            if current.key == key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return None

    def delete(self, key):
        parent = None
        current = self.root

        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            print("no key")
            return
        #case 1 nema djece
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        #case 2 dva djeteta
        elif current.left and current.right:
            predecessor_parent = current
            predecessor = current.left
            #logika maxvaluenode
            while predecessor.right is not None:
                predecessor_parent = predecessor
                predecessor = predecessor.right

            current.key = predecessor.key
            current.value = predecessor.value

            if predecessor_parent.left == predecessor:
                predecessor_parent.left = predecessor.left
            else:
                predecessor_parent.right = predecessor.left
        #case 3 jeno dijete
        else:
            child = current.left if current.left else current.right

            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

    def in_order_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node is None:
            return result

        if node.left is not None:
            self.in_order_traversal(node.left, result)

        result.append((node.key, node.value))

        if node.right is not None:
            self.in_order_traversal(node.right, result)

        return result

    def max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def max_value_leaf(self, node):
        if node is None:
            return None
        current = node
        while current.left is not None or current.right is not None:
            if current.right is not None:
                current = current.right
            else:
                current = current.left
        return current.key
