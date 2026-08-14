CONTAINS:
BUBBLE - ARR - SINGLE - DOUBLE
MERGE - ARR - SINGLE - DOUBLE
SELECTION - ARR - SINGLE - DOUBLE 
QUICK - ARR - SINGLE - DOUBLE
QUICK_2 - ARR
INSERTION - ARR - SINGLE - DOUBLE
BUCKET - ARR - SINGLE - DOUBLE


Bubble
Array
Singly-linked: data-swap
Doubly-linked: data-swap
Singly-linked: pointer-swap
Doubly-linked: pointer-swap

# VAŽNO: Verzije 3 i 4 (dvostruko povezane liste) imaju smisla samo ako nam 
# trebaju .prev pokazivači za druge operacije (npr. brisanje, umetanje s lijeva).
# Ako nam .prev ne treba, jednostruka lista (Verzija 1 ili 2, data sawp) je bolji izbor 
# jer troši manje memorije i jednostavnija je za održavanje.

#BUBBLE SORT
# Normalno (niz / array)

def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:    # ascending order (flip sign for descending )
                arr[i-1], arr[i] = arr[i], arr[i-1] # zamjena elemenata
                swapped = True
        if not swapped: 
            break
    return arr
  
# BUBBLE SINGLE data-swap
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
                if current.data < next_node.data: # descending
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = current.next

#BUBBLE DOUBLE data-swap
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


# sinlge libked pointer swap
    def bubble_sort_pointer_swap(self):
        """Sortira listu silazno koristeći zamjenu pokazivača (pointer swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            prev = None  # Prati čvor koji se nalazi ispred 'current'
            
            while current.next is not None:
                next_node = current.next
                
                # Silazni poredak
                if current.data < next_node.data:
                    swapped = True
                    
                    # PRESPOJAVANJE POKAZIVAČA:
                    current.next = next_node.next
                    next_node.next = current
                    
                    # Ako smo mijenjali prva dva čvora u listi, moramo ažurirati 'self.head'
                    if prev is None:
                        self.head = next_node
                    else:
                        prev.next = next_node
                    
                    # Nakon zamjene, čvorovi su zamijenili mjesta u memoriji.
                    # 'next_node' je sada ispred 'current', pa 'prev' postaje 'next_node'.
                    prev = next_node
                    # current ostaje isti (sada je iza next_node)
                else:
                    # Ako nije bilo zamjene, samo pomičemo oba pokazivača naprijed
                    prev = current
                    current = current.next
                    
# double poniter sawp
    def bubble_sort_pointer_swap(self):
        """Sortira dvostruko povezanu listu silazno koristeći zamjenu pokazivača (pointer swap)."""
        if self.head is None or self.head.next is None:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next is not None:
                next_node = current.next
                if current.data < next_node.data:   # descending
                    swapped = True
                    left = current.prev
                    right = next_node.next

                    # put next_node before current
                    next_node.next = current
                    current.prev = next_node

                    # connect current to right
                    current.next = right
                    if right is not None:
                        right.prev = current

                    # connect next_node to left
                    next_node.prev = left
                    if left is not None:
                        left.next = next_node
                    else:
                        # next_node becomes new head
                        self.head = next_node

                    # advance current to the node after the swapped current
                    current = current.next
                else:
                    current = current.next
