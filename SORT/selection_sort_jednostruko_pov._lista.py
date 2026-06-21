def selection_sort_singly(head):
    i = head                            # for i in range(n):
    while i:
        min_node = i                    # min_idx = i
        
        j = i.next                      # for j in range(i + 1, n):
        while j:
            if j.data < min_node.data:  # if arr[j] < arr[min_idx]:
                min_node = j            # min_idx = j
            j = j.next
            
        # Profesorov trik: zamijeni samo podatke (arr[i], arr[min_idx] = ...)
        i.data, min_node.data = min_node.data, i.data
        i = i.next
        
    return head
