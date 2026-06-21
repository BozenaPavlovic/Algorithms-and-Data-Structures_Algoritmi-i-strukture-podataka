class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def get_middle(head):
    """Pronalazi sredinu liste pomoću 'Zec i kornjača' metode"""
    if not head:
        return head
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    """Spaja dvije sortirane liste preusmjeravanjem pokazivača"""
    dummy = Node(0)
    current = dummy
    
    while left and right:
        if left.data <= right.data:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next
        current = current.next
        
    if left:
        current.next = left
    if right:
        current.next = right
        
    return dummy.next

def merge_sort_linked_list(head):
    # Bazni slučaj: ako je lista prazna ili ima 1 element
    if not head or not head.next:
        return head
        
    # 1. Pronađi sredinu i prereži listu na pola
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None  # Ovdje prekidamo listu na dva dijela
    
    # 2. Rekurzivno sortiraj lijevu i desnu polovinu
    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)
    
    # 3. Spoji ih natrag
    return merge(left, right)
