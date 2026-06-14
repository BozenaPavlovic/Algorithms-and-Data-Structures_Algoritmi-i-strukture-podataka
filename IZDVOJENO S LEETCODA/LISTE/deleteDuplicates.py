def deleteDuplicates(head):
    curr = head

    while curr is not None and curr.next is not None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next  # Preskoči duplikat
        else:
            curr = curr.next  # Pomakni se naprijed samo ako nema duplikata

    return head