# Python Program for merge sort on doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to split the doubly linked
# list into two halves
def split(head):
    fast = head
    slow = head

    # Move fast pointer two steps and slow pointer
    # one step until fast reaches the end
    while fast is not None and fast.next is not None \
    				and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    # Split the list into two halves
    temp = slow.next
    slow.next = None
    if temp is not None:
        temp.prev = None
    return temp

# Function to merge two sorted doubly linked lists
def merge(first, second):

    # If either list is empty, return the other list
    if first is None:
        return second
    if second is None:
        return first

    # Pick the smaller value between first
    # and second nodes
    if first.data < second.data:

        # Recursively merge the rest of the lists
        # and link the result to the current node
        first.next = merge(first.next, second)
        if first.next is not None:
            first.next.prev = first
        first.prev = None
        return first
    else:

        # Recursively merge the rest of the lists and
        # link the result to the current node
        second.next = merge(first, second.next)
        if second.next is not None:
            second.next.prev = second
        second.prev = None
        return second

# Function to perform merge sort on a
# doubly linked list
def MergeSort(head):

    # Base case: if the list is empty or has only
    # one node, it's already sorted
    if head is None or head.next is None:
        return head

    # Split the list into two halves
    second = split(head)

    # Recursively sort each half
    head = MergeSort(head)
    second = MergeSort(second)

    # Merge the two sorted halves
    return merge(head, second)


def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":

    # Create a hard-coded doubly linked list:
    # 10 <-> 8 <-> 5 <-> 2
    head = Node(10)
    head.next = Node(8)
    head.next.prev = head
    head.next.next = Node(5)
    head.next.next.prev = head.next
    head.next.next.next = Node(2)
    head.next.next.next.prev = head.next.next

    head = MergeSort(head)

    printList(head)
