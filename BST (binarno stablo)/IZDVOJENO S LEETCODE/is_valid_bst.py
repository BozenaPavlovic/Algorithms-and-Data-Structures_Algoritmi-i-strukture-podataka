# https://leetcode.com/problems/validate-binary-search-tree/description/
# 98. Validate Binary Search Tree

# https://www.youtube.com/watch?v=nTXuWuqIka4


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, minn, maxx):
            if not node:
                return True
            
            if node.val <= minn or node.val >= maxx:
                return False
            
            return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)

        return is_valid(root, float("-inf"), float("inf"))

# Time Complexity: O(n)
# Space Complexity: O(h) { here "h" is height of tree }


# Bootcamp solution
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stk = [(root, float('-inf'), float('inf'))]

        while stk:
            node, minn, maxx = stk.pop()

            if node.val <= minn or node.val >= maxx:
                return False
            else:
                if node.left:
                    stk.append((node.left, minn, node.val))
                
                if node.right:
                    stk.append((node.right, node.val, maxx))
        
        return True
# Time Complexity: O(n)
# Space Complexity: O(h) { here "h" is height of tree }
