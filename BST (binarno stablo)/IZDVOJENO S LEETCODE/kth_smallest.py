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
                return 0
            if node.left is not None:
                inorder(node.left)
            list_num.append(node.val)
            if node.right is not None:
                inorder(node.right)
        inorder(root)
        return list_num[k-1]
