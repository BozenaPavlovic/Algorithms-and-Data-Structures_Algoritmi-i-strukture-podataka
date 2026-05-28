#Dvostruko povezana lista ( ISTO KOA I JEDNOSTRUKO POVEZANA !!!!)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None   # NOVO

class DoublyLinkedList:
    def __init__(self):
        self.head = None

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

