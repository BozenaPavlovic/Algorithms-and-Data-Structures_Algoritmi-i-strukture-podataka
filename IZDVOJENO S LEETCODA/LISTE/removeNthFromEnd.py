def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)  # Dummy rješava problem ako brišemo prvi element
    slow = dummy
    fast = dummy

    # Pomakni fast pokazivač za n koraka unaprijed
    for i in range(n):
        fast = fast.next

    # Pomiči oba pokazivača dok fast ne dođe do zadnjeg čvora
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    # Izbaci N-ti čvor s kraja (preskoči ga)
    slow.next = slow.next.next

    return dummy.next