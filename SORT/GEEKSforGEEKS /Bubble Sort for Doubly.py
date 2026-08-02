#https://www.geeksforgeeks.org/dsa/bubble-sort-on-doubly-linked-list/
# Python program to sort a doubly linked list using
# bubble sort

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to sort the linked list using bubble sort
def bubble_sort(head):
    if not head:
        return head

    swapped = True
    last = None

    # Keep going until no swaps occur in a pass
    while swapped:
        swapped = False
        curr = head

        # Traverse through the list and swap adjacent
        # nodes if they are in the wrong order
        while curr.next != last:
            if curr.data > curr.next.data:
              
                # Swap the data of the current node
                # and next node
                curr.data, curr.next.data = (
                    curr.next.data, curr.data
                )
                swapped = True
            curr = curr.next

        # Reduce the effective list size after each pass
        last = curr

    return head

def print_list(node):
    curr = node
    while curr:
        print(curr.data, end=" ")
        curr = curr.next

if __name__ == '__main__':
  
    # Create a hard-coded doubly linked list:
    # 5 <-> 3 <-> 4 <-> 1 <-> 2
    head = Node(5)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next
    head.next.next.next = Node(1)
    head.next.next.next.prev = head.next.next
    head.next.next.next.next = Node(2)
    head.next.next.next.next.prev = head.next.next.next

    head = bubble_sort(head)
    print_list(head)
