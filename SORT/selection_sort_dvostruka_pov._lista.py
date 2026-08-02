class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
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





# DOUBLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def selection_sort(head):
    if head is None or head.next is None:
        return head

    tail = None
    current = head

    while current is not None:
        small = current
        prev_small = None
        prev = current
        temp = current.next

        # Traži minimum (isti kod kao za jednostruku)
        while temp is not None:
            if temp.data < small.data:
                small = temp
                prev_small = prev
            prev = temp
            temp = temp.next

        # Izbaci minimum (isti kod)
        if small == current:
            current = current.next
        else:
            prev_small.next = small.next
            if small.next is not None:
                small.next.prev = prev_small   # 🟢 DODATAK za dvostruku

        # Dodaj minimum na kraj
        if tail is None:
            head = small
            small.prev = None                  # 🟢 DODATAK za dvostruku
        else:
            tail.next = small
            small.prev = tail                  # 🟢 DODATAK za dvostruku

        tail = small

    return head












