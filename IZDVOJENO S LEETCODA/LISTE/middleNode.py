def middleNode(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next  # Kornjača
        fast = fast.next.next  # Zec

    return slow