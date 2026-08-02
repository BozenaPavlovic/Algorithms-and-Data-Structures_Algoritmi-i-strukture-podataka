# https://www.geeksforgeeks.org/dsa/python-program-for-insertion-sort-in-a-singly-linked-list/




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertion_sort_linked_list(head):
    sorted_list = None
    current = head
    
    while current is not None:
        # Store next node to avoid losing reference
        next_node = current.next
        
        # Insert current node into the sorted list
        if sorted_list is None or current.data < sorted_list.data:
            current.next = sorted_list
            sorted_list = current
        else:
            # Find the correct position in the sorted list
            before = sorted_list
            while before.next is not None and before.next.data < current.data:
                before = before.next
            current.next = before.next
            before.next = current
        
        # Move to the next node in the original list
        current = next_node
        
    return sorted_list

# Example Usage
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> " if temp.next else "\n")
        temp = temp.next

# Create list: 5 -> 3 -> 4 -> 1 -> 2
head = Node(5)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)

print("Unsorted:")
print_list(head)

head = insertion_sort_linked_list(head)

print("Sorted:")
print_list(head)   
