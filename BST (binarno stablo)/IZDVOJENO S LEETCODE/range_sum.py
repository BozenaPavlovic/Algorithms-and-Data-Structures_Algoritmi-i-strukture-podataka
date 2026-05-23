# https://leetcode.com/problems/range-sum-of-bst/description/
# 938. Range Sum of BST

def range_sum(self, low, high, node=None):
    if node is None:
        node = self.root
    if node is None:
        return 0

    # Ako je trenutni čvor manji od low → idi desno (tamo su veći)
    if node.key < low:
        return self.range_sum(low, high, node.right)

    # Ako je trenutni čvor veći od high → idi lijevo (tamo su manji)
    if node.key > high:
        return self.range_sum(low, high, node.left)

    # Inače, čvor je unutar [low, high] → zbroji njega + lijevo + desno
    return (node.key +
            self.range_sum(low, high, node.left) +
            self.range_sum(low, high, node.right))