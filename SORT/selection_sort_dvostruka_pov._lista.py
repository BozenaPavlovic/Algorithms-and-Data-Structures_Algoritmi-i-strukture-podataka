def selection_sort_doubly(head):
    i = head
    while i:
        min_node = i
        
        j = i.next
        while j:
            if j.data < min_node.data:
                min_node = j
            j = j.next
            
        # Zamjena podataka unutar čvorova
        i.data, min_node.data = min_node.data, i.data
        i = i.next
        
    return head
