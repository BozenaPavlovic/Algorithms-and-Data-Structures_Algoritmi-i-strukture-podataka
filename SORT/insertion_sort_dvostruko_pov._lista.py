def insertion_sort_doubly(head):
    if not head: return head, 0
    swaps = 0
    current = head.next  # range(1, len(arr))
    
    while current:
        key = current.data
        j = current.prev
        
        while j and j.data > key:
            j.next.data = j.data  # arr[j + 1] = arr[j]
            swaps += 1
            j = j.prev            # j -= 1
            
        if j:
            j.next.data = key     # arr[j + 1] = key
        else:
            head.data = key       # Ako smo došli do samog početka
        swaps += 1
        
        current = current.next
        
    return head, swaps
