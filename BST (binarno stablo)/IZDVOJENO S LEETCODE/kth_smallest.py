# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# 230. Kth Smallest Element in a BST

def kth_smallest(self, k, node=None, counter=None):
    if node is None:
        node = self.root
    if counter is None:
        counter = [0]  # koristimo listu da prođemo po referenci

    # IN-ORDER obilazak (L → N → R)
    result = self._inorder_kth(node, k, counter)
    return result


def _inorder_kth(self, node, k, counter):
    if node is None:
        return None

    # Lijevo
    left_result = self._inorder_kth(node.left, k, counter)
    if left_result is not None:
        return left_result

    # Čvor (broji)
    counter[0] += 1
    if counter[0] == k:
        return node.key

    # Desno
    return self._inorder_kth(node.right, k, counter)


def kth_smallest_ALT(self, k):
    # In-order obilazak vraća sortiranu listu
    sorted_nodes = self.inorder()  # tvoja postojeca funkcija
    return sorted_nodes[k-1] if k <= len(sorted_nodes) else None