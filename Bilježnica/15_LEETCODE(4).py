Leetcode – preporučeni zadaci za vježbu
▪ Osnove rekurzije
 206. Reverse Linked List — Easy, rekurzivno okretanje liste
 344. Reverse String — Easy, rekurzija na arrayu
▪ Divide & Conquer
 21. Merge Two Sorted Lists — Easy, rekurzivno spajanje
 50. Pow(x, n) — Medium, brzo vs. sporo potenciranje rekurzijom
 240. Search a 2D Matrix II — Medium
▪ Bonus (backtracking)
 78. Subsets — Medium, generiranje svih podskupova
▪ Obratite pozornost na zadatak 50. koji se može riješiti na sporiji (linearno) i brži (logaritamski)
način – iza 1. lab. vježbe ćemo pričati više o složenosti (linearno vs. logaritamski, itd.)


206. Reverse Linked List — Easy, rekurzivno okretanje liste
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):

        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head

344. Reverse String — Easy, rekurzija na arrayu Divide & Conquer
# IN PLACE 
class Solution(object):
    def reverseString(self, s):
        def reverse(left, right):
            # ako smo došli do sredine, gotovo
            if left >= right:
                return
            # zamijeni prvi i zadnji znak
            s[left], s[right] = s[right], s[left]
            # pomakni se prema sredini
            reverse(left + 1, right - 1)
        reverse(0, len(s) - 1)
        
21. Merge Two Sorted Lists — Easy, rekurzivno spajanje
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
            
50. Pow(x, n) — Medium, brzo vs. sporo potenciranje rekurzijom
240. Search a 2D Matrix II — Medium
78. Subsets — Medium, generiranje svih podskupova
