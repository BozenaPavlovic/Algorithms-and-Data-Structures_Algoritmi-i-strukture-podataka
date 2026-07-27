class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def selection_sort(head):
    if head is None or head.next is None:
        return head
    
    start = head
    while start is not None and start.next is not None:
        min_node = start
        current = start.next
        
        while current is not None:
            if current.data < min_node.data:
                min_node = current
            current = current.next
        
        if min_node != start:
            start.data, min_node.data = min_node.data, start.data
        
        start = start.next
    
    return head
