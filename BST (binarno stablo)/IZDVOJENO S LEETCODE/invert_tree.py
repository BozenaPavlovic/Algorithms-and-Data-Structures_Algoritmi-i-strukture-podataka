# https://leetcode.com/problems/invert-binary-tree/description/
# 226. Invert Binary Tree

def invert_tree(self, node=None):
    if node is None:
        node = self.root
    if node is None:
        return None

    # Zamijeni lijevo i desno
    node.left, node.right = node.right, node.left

    # Rekurzivno invertiraj podstabla
    self.invert_tree(node.left)
    self.invert_tree(node.right)

    return node