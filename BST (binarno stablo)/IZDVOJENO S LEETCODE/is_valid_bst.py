# https://leetcode.com/problems/validate-binary-search-tree/description/
# 98. Validate Binary Search Tree



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        # Pomoćna funkcija koja prati trenutni čvor i njegove granice
        def validate(node, low, high):
            # 1. Bazni slučaj: Prazno stablo je uvijek validan BST
            if node is None:
                return True
            
            # 2. Provjera krši li trenutni čvor granice
            # Vrijednost mora biti strogo veća od low i strogo manja od high
            if node.val <= low or node.val >= high:
                return False
            
            # 3. Rekurzivni korak za lijevo i desno podstablo
            # Za lijevo dijete: gornja granica postaje trenutni node.val
            # Za desno dijete: donja granica postaje trenutni node.val
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Na samom početku, korijen može imati bilo koju vrijednost
        # Koristimo float('-inf') i float('inf') za minus i plus beskonačno
        return validate(root, float('-inf'), float('inf'))
