Leetcode – preporučeni zadaci za vježbu
▪ Osnovno obilaženje (rekurzija na stablu)
 226. Invert Binary Tree — Easy, zamijeni lijevo/desno dijete pa rekurziraj
 938. Range Sum of BST — Easy, rekurzivno zbrajanje vrijednosti unutar raspona [low, high] BST
svojstvo dopušta da preskočimo cijela podstabla izvan raspona → ne moramo obići svaki čvor
▪ BST svojstva na djelu
 230. Kth Smallest Element in a BST — Medium, in-order obilazak daje sortirani redoslijed
 98. Validate Binary Search Tree — Medium, provjera invarijante provlačenjem granica (min,
max) kroz rekurziju
▪ Obratite pozornost na zadatak 98. koji pokazuje da lokalna provjera (samo roditelj vs.
neposredno dijete) nije dovoljna — invarijantu treba provući kroz cijelu rekurziju u obliku
gornje i donje granice.




226. Invert Binary Tree — Easy, zamijeni lijevo/desno dijete pa 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
            
# 1. base case
# 2. napravi nešto s trenutnim čvorom
# 3. rekurzija lijevo
# 4. rekurzija desno
# 5. return

938. Range Sum of BST — Easy, rekurzivno zbrajanje vrijednosti unutar raspona [low, high] BST
svojstvo dopušta da preskočimo cijela podstabla izvan raspona → ne moramo obići svaki čvor
▪ BST svojstva na djelu
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root is None:
            return 0
        if root.val  < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left,low, high)

        return root.val + self.rangeSumBST(root.left,low, high) + self.rangeSumBST(root.right, low, high)

      

230. Kth Smallest Element in a BST — Medium, in-order obilazak daje sortirani redoslijed
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
      
98. Validate Binary Search Tree — Medium, provjera invarijante provlačenjem granica (min,
max) kroz rekurziju
▪ Obratite pozornost na zadatak 98. koji pokazuje da lokalna provjera (samo roditelj vs.
neposredno dijete) nije dovoljna — invarijantu treba provući kroz cijelu rekurziju u obliku
gornje i donje granice.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def valid(node, minn, maxx):
            if node is None:
                return True
            if node.val <= minn or node.val >= maxx:
                return False
            return valid(node.left, minn, node.val) and valid(node.right, node.val, maxx)

        return valid(root, float("-inf"), float("inf"))
