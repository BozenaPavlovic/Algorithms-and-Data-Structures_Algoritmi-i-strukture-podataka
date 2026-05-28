#(jednostruko povezana lista, silazno)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None    ## OVODNO


    def bubble_sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head

            while current.next:
                next_node = current.next
                if current.data < next_node.data:  # silazno
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next
