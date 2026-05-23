def lowest_common_ancestor(self, p, q, node=None):
    if node is None:
        node = self.root

    # Ako su oba manja od trenutnog → LCA je lijevo
    if p < node.key and q < node.key:
        return self.lowest_common_ancestor(p, q, node.left)

    # Ako su oba veća od trenutnog → LCA je desno
    if p > node.key and q > node.key:
        return self.lowest_common_ancestor(p, q, node.right)

    # Inače, trenutni čvor je LCA (jedan je lijevo, drugi desno)
    return node.key