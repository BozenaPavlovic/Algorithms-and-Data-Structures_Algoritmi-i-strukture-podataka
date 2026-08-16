Leetcode – preporučeni zadaci za vježbu
▪ Osnove
 206. Reverse Linked List — Easy
 83. Remove Duplicates from Sorted List — Easy
▪ Rad s dva „pokazivača”
 876. Middle of the Linked List— Easy
▪ Malo zanimljiviji zadaci
 21. Merge Two Sorted Lists — Easy
 19. Remove Nth Node From End of List — Medium, rješenje s dva pokazivača, slično kao 876.
 2. Add Two Numbers — Medium, lista kao reprezentacija cijelog broja!
▪ Neki od ovih zadataka se mogu riješiti na vremenski učinkovit ili manje učinkovit način,
ovisno o implementaciji




206. Reverse Linked List — Easy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        curr = head
        prev= None
        while curr is not None:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next



  

            
        return prev
