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
#DOUBLY 
class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
class Solution(object):
    def reverseList(self, head):
        curr = head

        while curr is not None:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev

        return head

83. Remove Duplicates from Sorted List — Easy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return None
        curr = head
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
        
#DOUBLY 
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def deleteDuplicates(head):
    if head is None:
        return None
    curr = head
    while curr is not None and curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next

            if curr.next is not None:
                curr.next.prev = curr
        else:
            curr = curr.next
    return head

 876. Middle of the Linked List— Easy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if head is None:
            return None
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

21. Merge Two Sorted Lists — Easy
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

        dummy = ListNode()
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1 is None:
            curr.next = list2
        else:
            curr.next = list1
        return dummy.next


19. Remove Nth Node From End of List 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None:
            return None

        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return dummy.next

2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 is not None or l2 is not None:

            if l1 is not None:
                x = l1.val
                l1 = l1.next
            else:
                x = 0

            if l2 is not None:
                y = l2.val
                l2 = l2.next
            else:
                y = 0

            result = x + y + carry

            digit = result % 10
            carry = result // 10

            curr.next = ListNode(digit)
            curr = curr.next

        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next
