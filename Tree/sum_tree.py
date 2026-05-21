# rekurzivnu funkciju sum_tree(node) koja vraća zbroj svih vrijednosti u stablu

def sum_tree(node):
    if node is None:
        return 0
    return node.key + sum_tree(node.left) + sum_tree(node.right)
