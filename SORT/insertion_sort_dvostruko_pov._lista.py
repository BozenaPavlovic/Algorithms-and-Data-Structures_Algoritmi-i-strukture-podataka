class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertion_sort_doubly_linked_list(head):
    if head is None:
        return None
        
    sorted_list = None
    current = head
    
    while current is not None:
        # Store next node to avoid losing reference
        next_node = current.next
        
        # Detach current node from the original list
        current.prev = None
        current.next = None
        
        # Insert current node into the sorted list
        if sorted_list is None or current.data < sorted_list.data:
            # Insert at the beginning
            current.next = sorted_list
            if sorted_list:
                sorted_list.prev = current
            sorted_list = current
        else:
            # Find the correct position in the sorted list
            before = sorted_list
            while before.next is not None and before.next.data < current.data:
                before = before.next
            
            # Insert after 'before'
            current.next = before.next
            current.prev = before
            if before.next:
                before.next.prev = current
            before.next = current
        
        # Move to the next node in the original list
        current = next_node
        
    return sorted_list

# Example Usage
def print_list_forward(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> " if temp.next else "\n")
        temp = temp.next

# Create list: 5 <-> 3 <-> 4 <-> 1 <-> 2
head = Node(5)
node3 = Node(3)
node4 = Node(4)
node1 = Node(1)
node2 = Node(2)

head.next = node3
node3.prev = head
node3.next = node4
node4.prev = node3
node4.next = node1
node1.prev = node4
node1.next = node2
node2.prev = node1
