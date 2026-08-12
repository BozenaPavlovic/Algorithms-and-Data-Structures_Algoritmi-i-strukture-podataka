CONTAINS:
BUBBLE - ARR - SINGLE - DOUBLE
MERGE - ARR - SINGLE - DOUBLE
SELECTION - ARR - SINGLE - DOUBLE 


Bubble
Array
Singly-linked: data-swap
Doubly-linked: data-swap



#BUBBLE SORT
# Normalno (niz / array)

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1] # zamjena elemenata
                swapped = True
        if not swapped:
            break
    return arr
  
# BUBBLE SINGLE
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def bubble_sort_data_swap(self):
        """Sortira listu silazno koristeći zamjenu podataka (data swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                next_node = current.next
                # Silazni poredak: ako je trenutni manji od idućeg, mijenjaj podatke
                if current.data < next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next

#BUBBLE DOUBLE
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def bubble_sort_data_swap(self):
        """Sortira dvostruko povezanu listu silazno koristeći zamjenu podataka (data swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                next_node = current.next
                # Silazni poredak: ako je trenutni manji od idućeg, mijenjaj podatke
                if current.data < next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next




