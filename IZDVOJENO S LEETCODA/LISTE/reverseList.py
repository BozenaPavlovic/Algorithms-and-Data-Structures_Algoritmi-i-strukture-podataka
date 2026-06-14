def reverseList(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next  # Privremeno spremi ostatak liste
        curr.next = prev  # Okreni pokazivač unazad
        prev = curr  # Pomakni 'prev' na trenutni čvor
        curr = next_node  # Pomakni 'curr' na sljedeći čvor

    return prev  # 'prev' je nova glava okrenute liste