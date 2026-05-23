def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        node = self.root
    if node is None:
        return True

    # Trenutni čvor mora biti unutar [min_val, max_val]
    if not (min_val < node.key < max_val):
        return False

    # Lijevo podstablo: sve vrijednosti moraju biti MANJE od node.key
    # Desno podstablo: sve vrijednosti moraju biti VEĆE od node.key
    return (self.is_valid_bst(node.left, min_val, node.key) and
            self.is_valid_bst(node.right, node.key, max_val))