# https://leetcode.com/problems/range-sum-of-bst/description/
# 938. Range Sum of BST

class Solution(object):
    def rangeSumBST(self, root, low, high):
        # 1. Bazni slučaj: ako je čvor prazan, on doprinosi sa 0 u zbroj
        if root is None:
            return 0
        
        # 2. Ako je trenutni čvor PREMALI, njegova lijeva strana je isto premala.
        # Zato ignoriramo lijevo i samo nastavljamo tražiti desno.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
            
        # 3. Ako je trenutni čvor PREVELIK, njegova desna strana je isto prevelika.
        # Zato ignoriramo desno i samo nastavljamo tražiti lijevo.
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
            
        # 4. Ako smo stigli ovdje, znači da je trenutni čvor TAJ (unutar [low, high])!
        # Uzimamo njegovu vrijednost (root.val) i pribrajamo joj ono što nađemo
        # u lijevom i u desnom podstablu.
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
