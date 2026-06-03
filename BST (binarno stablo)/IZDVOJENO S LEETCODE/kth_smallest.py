# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        list_num=[]
        def inorder(node):
            if node is None:
                return None
            if node.left is not None:
                inorder(node.left)
            list_num.append(node.val)
            if node.right is not None:
                inorder(node.right)
        inorder(root)
        return list_num[k-1]




class Solution(object):
    def kthSmallest(self, root, k):
        # 1. Prazna lista za spremanje sortiranih brojeva
        list_num = []
        
        def inorder(node):
            # BAZNI SLUČAJ: Ako si došao na prazno mjesto, samo se vrati natrag (bez 0!)
            if node is None:
                return
            
            # 2. IN-ORDER REDOSLIJED (Lijevo -> Trenutni -> Desno)
            # Ne trebaju nam 'if' uvjeti za djecu, samo ih pozovemo.
            # Ako je dijete None, funkcija će se pokrenuti i odmah stati na liniji 9.
            inorder(node.left)          # Idi skroz lijevo
            list_num.append(node.val)   # Spremi trenutni broj
            inorder(node.right)         # Idi desno

        # 3. Pokrenemo rekurziju od korijena
        inorder(root)
        
        # 4. Vraćamo k-ti najmanji element (indeks k-1 jer liste kreću od 0)
        return list_num[k - 1]
