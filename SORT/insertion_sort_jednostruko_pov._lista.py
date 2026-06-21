def insertion_sort_singly(head):
    if not head: 
        return head
        
    i = head.next
    while i:
        j = head
        while j != i:
            if j.data > i.data:  # Ako je element prije veći, zamijeni podatke
                j.data, i.data = i.data, j.data
            j = j.next
        i = i.next
        
    return head
