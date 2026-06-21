def insertion_sort_singly(head):
    swaps = 0
    i = head
    
    while i:
        j = head
        while j != i:
            if j.data > i.data:
                # Zamjena vrijednosti (kao u nizu)
                j.data, i.data = i.data, j.data
                swaps += 1
            j = j.next
        i = i.next
        
    return head, swaps
